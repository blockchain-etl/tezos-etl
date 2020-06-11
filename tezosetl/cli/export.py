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

from tezosetl.jobs.export_job import ExportJob

from tezosetl.jobs.exporters.tezos_item_exporter import TezosItemExporter
from tezosetl.rpc.tezos_rpc import TezosRpc
from blockchainetl_common.logging_utils import logging_basic_config
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start-block', default=0, show_default=True, type=int, help='Start block')
@click.option('-e', '--end-block', required=True, type=int, help='End block')
@click.option('-p', '--provider-uri', default='https://mainnet-tezos.giganode.io', show_default=True, type=str,
              help='The URI of the remote Tezos node')
@click.option('-w', '--max-workers', default=5, show_default=True, type=int, help='The maximum number of workers.')
@click.option('-o', '--output-dir', default=None, type=str, help='The output directory for block data.')
def export(start_block, end_block, provider_uri, max_workers, output_dir):
    """Export block data."""

    job = ExportJob(
        start_block=start_block,
        end_block=end_block,
        tezos_rpc=ThreadLocalProxy(lambda: TezosRpc(provider_uri)),
        max_workers=max_workers,
        item_exporter=TezosItemExporter(output_dir),
    )
    job.run()
