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

from tezosetl.utils.cast_utils import safe_int


def map_balance_updates(block, response):
    for balance_update in yield_balance_updates(response):
        yield map_balance_update(block, balance_update)


def yield_balance_updates(response):
    metadata = response.get('metadata')

    # from block
    if metadata is not None:
        balance_updates = metadata.get('balance_updates', [])
        for balance_update in balance_updates:
            yield {
                'type': 'block',
                'operation_hash': None,
                'balance_update': balance_update
            }

    # from operations
    for operation_group in response.get('operations', []):
        for operation in operation_group:
            operation_hash = operation.get('hash')
            for content in operation.get('contents', []):
                metadata = content.get('metadata')
                if metadata is not None:
                    for balance_update in metadata.get('balance_updates', []):
                        yield {
                            'type': 'operation',
                            'operation_hash': operation_hash,
                            'balance_update': balance_update
                        }


def map_balance_update(block, balance_update):
    return {
        'item_type': 'balance_update',
        'level': block.get('level'),
        'timestamp': block.get('timestamp'),
        'block_hash': block.get('block_hash'),
        'type': balance_update.get('type'),
        'operation_hash': balance_update.get('operation_hash'),
        'kind': balance_update['balance_update'].get('kind'),
        'contract': balance_update['balance_update'].get('contract'),
        'change': safe_int(balance_update['balance_update'].get('change')),
        'delegate': balance_update['balance_update'].get('delegate'),
        'category': balance_update['balance_update'].get('category'),
    }
