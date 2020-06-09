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

import pytest

from tezosetl.enums.operations_types import OperationType
from tezosetl.jobs.export_blocks_job import ExportBlocksJob
from tezosetl.jobs.exporters.tezos_item_exporter import TezosItemExporter
from tests.tezosetl.helpers import get_tezos_rpc
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

import tests.resources
from tests.helpers import compare_lines_ignore_order, read_file, skip_if_slow_tests_disabled

RESOURCE_GROUP = 'test_export_blocks_job'


def read_resource(resource_group, file_name):
    return tests.resources.read_resource([RESOURCE_GROUP, resource_group], file_name)


@pytest.mark.parametrize("start_block, end_block, resource_group ,provider_type", [
    (417645, 417645, 'tezos/block_417645', 'mock'),
    skip_if_slow_tests_disabled([417645, 417645, 'tezos/block_417645', 'online']),
])
def test_export_blocks_job(tmpdir, start_block, end_block, resource_group, provider_type):
    job = ExportBlocksJob(
        start_block=start_block,
        end_block=end_block,
        tezos_rpc=ThreadLocalProxy(
            lambda: get_tezos_rpc(
                provider_type,
                read_resource_lambda=lambda file: read_resource(resource_group, file))),
        max_workers=5,
        item_exporter=TezosItemExporter(str(tmpdir)),
    )
    job.run()

    all_files = ['block.json', 'balance_update.json'] + \
                [f'{operation_type}_operation.json' for operation_type in OperationType.ALL]

    for file in all_files:
        print('=====================')
        print(read_file(str(tmpdir.join(file))))
        compare_lines_ignore_order(
            read_resource(resource_group, f'expected_{file}'), read_file(str(tmpdir.join(file)))
        )
