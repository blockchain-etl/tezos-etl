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
from tezosetl.utils.date_utils import convert_timestr_to_timestamp


def map_block(response):
    block = {}
    block['type'] = 'block'
    block['protocol'] = response.get('protocol')
    block['chain_id'] = response.get('chain_id')
    block['block_hash'] = response.get('hash')

    number_of_operations = 0
    for operation_group in response.get('operations', []):
        number_of_operations += len(operation_group)
    block['number_of_operation_groups'] = len(response.get('operations', []))
    block['number_of_operations'] = number_of_operations

    header = response.get('header')
    if header is not None:
        block['level'] = header.get('level')
        block['proto'] = header.get('proto')
        block['predecessor'] = header.get('predecessor')
        block['timestamp'] = convert_timestr_to_timestamp(header.get('timestamp')) * 1000
        block['validation_pass'] = header.get('validation_pass')
        block['operations_hash'] = header.get('operations_hash')
        block['fitness'] = header.get('fitness')
        block['context'] = header.get('context')

    metadata = response.get('metadata')
    if metadata is not None:
        block['nonce_hash'] = metadata.get('nonce_hash')
        block['consumed_gas'] = safe_int(metadata.get('consumed_gas'))
        block['baker'] = metadata.get('baker')
        block['voting_period_kind'] = metadata.get('voting_period_kind')

        level = metadata.get('level')

        if level is not None:
            block['cycle'] = level.get('cycle')
            block['cycle_position'] = level.get('cycle_position')
            block['voting_period'] = level.get('voting_period')
            block['voting_period_position'] = level.get('voting_period_position')
            block['expected_commitment'] = level.get('expected_commitment')

    return block
