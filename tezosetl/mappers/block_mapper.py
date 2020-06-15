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


def map_block(response):
    number_of_operations = count_operations(response.get('operations', EMPTY_LIST))

    header = response.get('header', EMPTY_OBJECT)
    metadata = response.get('metadata', EMPTY_OBJECT)
    level = metadata.get('level', EMPTY_OBJECT)

    block = {
        'item_type': 'block',
        'protocol': response.get('protocol'),
        'chain_id': response.get('chain_id'),
        'block_hash': response.get('hash'),
        'number_of_operation_groups': len(response.get('operations', EMPTY_LIST)),
        'number_of_operations': number_of_operations,
        'level': header.get('level'),
        'proto': header.get('proto'),
        'predecessor': header.get('predecessor'),
        'timestamp': header.get('timestamp'),
        'validation_pass': header.get('validation_pass'),
        'operations_hash': header.get('operations_hash'),
        'fitness': header.get('fitness'),
        'context': header.get('context'),
        'nonce_hash': metadata.get('nonce_hash'),
        'consumed_gas': safe_int(metadata.get('consumed_gas')),
        'baker': metadata.get('baker'),
        'voting_period_kind': metadata.get('voting_period_kind'),
        'cycle': level.get('cycle'),
        'cycle_position': level.get('cycle_position'),
        'voting_period': level.get('voting_period'),
        'voting_period_position': level.get('voting_period_position'),
        'expected_commitment': level.get('expected_commitment')
    }

    return block


def count_operations(operation_groups):
    number_of_operations = 0
    for operation_group in operation_groups:
        for operation in operation_group:
            number_of_operations += len(operation.get('contents', EMPTY_LIST))

            # Add internal operations
            for content in operation.get('contents', EMPTY_LIST):
                metadata = content.get('metadata', EMPTY_OBJECT)
                number_of_operations += len(metadata.get('internal_operation_results', EMPTY_LIST))

    return number_of_operations


EMPTY_OBJECT = {}
EMPTY_LIST = []
