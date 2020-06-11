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

import logging
import os
from time import time

from blockchainetl_common.logging_utils import logging_basic_config
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy
from tezosetl.jobs.export_job import ExportJob
from tezosetl.jobs.exporters.tezos_item_exporter import TezosItemExporter
from tezosetl.rpc.tezos_rpc import TezosRpc

logging_basic_config()
logger = logging.getLogger('export_partitioned')


def export_partitioned(partitions, output_dir, output_format, provider_uri, max_workers, batch_size):
    for batch_start_block, batch_end_block, partition_dir, *args in partitions:
        # # # start # # #

        start_time = time()

        padded_batch_start_block = str(batch_start_block).zfill(8)
        padded_batch_end_block = str(batch_end_block).zfill(8)
        block_range = '{padded_batch_start_block}-{padded_batch_end_block}'.format(
            padded_batch_start_block=padded_batch_start_block,
            padded_batch_end_block=padded_batch_end_block,
        )

        partition_output_dir = '{output_dir}/blocks{partition_dir}'.format(
            output_dir=output_dir,
            partition_dir=partition_dir,
        )
        os.makedirs(os.path.dirname(partition_output_dir), exist_ok=True)

        logger.info('Exporting blocks {block_range} to {partition_output_dir}'.format(
            block_range=block_range,
            partition_output_dir=partition_output_dir,
        ))

        job = ExportJob(
            start_block=batch_start_block,
            end_block=batch_end_block,
            batch_size=batch_size,
            tezos_rpc=ThreadLocalProxy(lambda: TezosRpc(provider_uri)),
            max_workers=max_workers,
            item_exporter=TezosItemExporter(partition_output_dir, output_format=output_format),
        )
        job.run()

        # # # finish # # #

        end_time = time()
        time_diff = round(end_time - start_time, 5)
        logger.info('Exporting blocks {block_range} took {time_diff} seconds'.format(
            block_range=block_range,
            time_diff=time_diff,
        ))
