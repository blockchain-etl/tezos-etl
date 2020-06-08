# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev evge.medvedev@gmail.com
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


import click

from tezosetl.jobs.export_blocks_job import ExportBlocksJob
from tezosetl.jobs.exporters.blocks_item_exporter import blocks_item_exporter
from tezosetl.rpc.tezos_rpc import TezosRpc
from blockchainetl_common.logging_utils import logging_basic_config
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start-block', default=0, type=int, help='Start block')
@click.option('-e', '--end-block', required=True, type=int, help='End block')
@click.option('-p', '--provider-uri', default='http://api.main.alohatezos.com', type=str,
              help='The URI of the remote Tezos node')
@click.option('-w', '--max-workers', default=5, type=int, help='The maximum number of workers.')
@click.option('--blocks-output', default=None, type=str,
              help='The output file for blocks. '
                   'If not provided blocks will not be exported. Use "-" for stdout')
@click.option('--transactions-output', default=None, type=str,
              help='The output file for transactions. '
                   'If not provided transactions will not be exported. Use "-" for stdout')
@click.option('--actions-output', default=None, type=str,
              help='The output file for actions. '
                   'If not provided transactions will not be exported. Use "-" for stdout')
def export_blocks(start_block, end_block, provider_uri,
                  max_workers, blocks_output, transactions_output, actions_output):
    """Export blocks, transactions and actions."""

    if blocks_output is None and transactions_output is None and actions_output is None:
        raise ValueError('Either --blocks-output or --transactions-output or --actions-output options must be provided')

    job = ExportBlocksJob(
        start_block=start_block,
        end_block=end_block,
        tezos_rpc=ThreadLocalProxy(lambda: TezosRpc(provider_uri)),
        max_workers=max_workers,
        item_exporter=blocks_item_exporter(blocks_output, transactions_output, actions_output),
        export_blocks=blocks_output is not None,
        export_transactions=transactions_output is not None,
        export_actions=actions_output is not None)
    job.run()
