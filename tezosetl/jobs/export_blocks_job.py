# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from tezosetl.mappers.block_mapper import map_block
from tezosetl.service.tezos_service import TezosService
from blockchainetl_common.executors.batch_work_executor import BatchWorkExecutor
from blockchainetl_common.jobs.base_job import BaseJob
from blockchainetl_common.utils import validate_range


# Exports blocks, transactions and actions
class ExportBlocksJob(BaseJob):
    def __init__(
            self,
            start_block,
            end_block,
            tezos_rpc,
            max_workers,
            item_exporter,
            batch_size=1):
        validate_range(start_block, end_block)
        self.start_block = start_block
        self.end_block = end_block

        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter

        self.tezos_service = TezosService(tezos_rpc)

    def _start(self):
        self.item_exporter.open()

    def _export(self):
        self.batch_work_executor.execute(
            range(self.start_block, self.end_block + 1),
            self._export_batch,
            total_items=self.end_block - self.start_block + 1
        )

    def _export_batch(self, block_number_batch):
        blocks = self.tezos_service.get_blocks(block_number_batch)
        for block in blocks:
            self._export_block(block)
            # self._export_transactions(block)

    def _export_block(self, block):
        self.item_exporter.export_item(map_block(block))

    def _export_transactions(self, block):
        for transaction in block['transactions']:
            self._export_transaction(transaction, block)

    def _export_transaction(self, transaction, block):
        transaction_dict = self.transaction_mapper.transaction_to_dict(transaction, block)

        self.item_exporter.export_item(transaction_dict)

        if isinstance(transaction.get('trx'), dict) \
                and transaction.get('trx').get('transaction') is not None \
                and transaction.get('trx').get('transaction').get('actions') is not None:
            for action in transaction.get('trx').get('transaction').get('actions'):
                action_dict = self.action_mapper.action_to_dict(action, transaction_dict)
                self.item_exporter.export_item(action_dict)

    def _end(self):
        self.batch_work_executor.shutdown()
        self.item_exporter.close()
