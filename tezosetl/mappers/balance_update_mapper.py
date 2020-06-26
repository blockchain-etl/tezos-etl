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
    # from block
    balance_updates = response.get('metadata', EMPTY_OBJECT).get('balance_updates', EMPTY_LIST)
    for balance_update_index, balance_update in enumerate(balance_updates):
        yield {
            'type': 'block',
            'balance_update': balance_update,
            'balance_update_index': balance_update_index,
        }

    # from operations
    for operation_group_index, operation_group in enumerate(response.get('operations', EMPTY_LIST)):
        for operation_index, operation in enumerate(operation_group):
            operation_hash = operation.get('hash')
            for content_index, content in enumerate(operation.get('contents', EMPTY_LIST)):
                metadata = content.get('metadata', EMPTY_OBJECT)
                metadata_balance_updates = metadata.get('balance_updates', EMPTY_LIST)
                for balance_update_index, balance_update in enumerate(metadata_balance_updates):
                    yield {
                        'type': 'operation_metadata',
                        'operation_hash': operation_hash,
                        'operation_group_index': operation_group_index,
                        'operation_index': operation_index,
                        'content_index': content_index,
                        'balance_update_index': balance_update_index,
                        'balance_update': balance_update
                    }

                operation_result = metadata.get('operation_result', EMPTY_OBJECT)
                operation_result_balance_updates = operation_result.get('balance_updates', EMPTY_LIST)
                for balance_update_index, balance_update in enumerate(operation_result_balance_updates):
                    yield {
                        'type': 'operation_result',
                        'operation_hash': operation_hash,
                        'operation_group_index': operation_group_index,
                        'operation_index': operation_index,
                        'content_index': content_index,
                        'balance_update_index': balance_update_index,
                        'status': operation_result.get('status'),
                        'balance_update': balance_update
                    }

                # from internal operations
                internal_operation_results = metadata.get('internal_operation_results', EMPTY_LIST)
                for internal_operation_index, internal_operation in enumerate(internal_operation_results):
                    result = internal_operation.get('result', EMPTY_OBJECT)
                    balance_updates = result.get('balance_updates', EMPTY_LIST)
                    for balance_update_index, balance_update in enumerate(balance_updates):
                        yield {
                            'type': 'internal_operation_result',
                            'operation_hash': operation_hash,
                            'operation_group_index': operation_group_index,
                            'operation_index': operation_index,
                            'content_index': content_index,
                            'internal_operation_index': internal_operation_index,
                            'balance_update_index': balance_update_index,
                            'status': result.get('status'),
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
        'operation_group_index': balance_update.get('operation_group_index'),
        'operation_index': balance_update.get('operation_index'),
        'content_index': balance_update.get('content_index'),
        'internal_operation_index': balance_update.get('internal_operation_index'),
        'balance_update_index': balance_update.get('balance_update_index'),
        'status': balance_update.get('status'),
        'kind': balance_update['balance_update'].get('kind'),
        'contract': balance_update['balance_update'].get('contract'),
        'change': safe_int(balance_update['balance_update'].get('change')),
        'delegate': balance_update['balance_update'].get('delegate'),
        'category': balance_update['balance_update'].get('category'),
    }


EMPTY_OBJECT = {}
EMPTY_LIST = []
