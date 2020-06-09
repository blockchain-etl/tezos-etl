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


def map_operations(block, response):
    for operation_group_id, operation_id, operation in yield_operations(response):
        for content in operation.get('contents', EMPTY_LIST):
            operation_kind = content.get('kind')
            base_operation = map_base_operation(block, operation_group_id, operation_id, operation, operation_kind)

            if operation_kind == 'endorsement':
                yield transform_endorsement(content, base_operation)
            elif operation_kind == 'transaction':
                yield transform_transaction(content, base_operation)
            elif operation_kind == 'delegation':
                yield transform_delegation(content, base_operation)
            elif operation_kind == 'reveal':
                yield transform_reveal(content, base_operation)
            elif operation_kind == 'seed_nonce_revelation':
                yield transform_seed_nonce_revelation(content, base_operation)
            elif operation_kind == 'activate_account':
                yield transform_activate_account(content, base_operation)
            elif operation_kind == 'origination':
                yield transform_origination(content, base_operation)
            elif operation_kind == 'proposals':
                yield transform_proposals(content, base_operation)
            elif operation_kind == 'double_baking_evidence':
                yield transform_double_baking_evidence(content, base_operation)
            elif operation_kind == 'double_endorsement_evidence':
                yield transform_double_endorsement_evidence(content, base_operation)
            elif operation_kind == 'ballot':
                yield transform_ballot(content, base_operation)
            else:
                print(content)
                print(base_operation)
                raise KeyError(f'Operation kind {operation_kind} not recognized')


def yield_operations(response):
    for operation_group_id, operation_group in enumerate(response.get('operations', EMPTY_LIST)):
        for operation_id, operation in enumerate(operation_group):
            yield operation_group_id, operation_id, operation


def map_base_operation(block, operation_group_id, operation_id, operation, operation_kind):
    return {
        'item_type': operation_kind + '_operation',
        'level': block.get('level'),
        'timestamp': block.get('timestamp'),
        'block_hash': block.get('block_hash'),
        'branch': operation.get('branch'),
        'signature': operation.get('signature'),
        'operation_hash': operation.get('hash'),
        'operation_group_id': operation_group_id,
        'operation_id': operation_id
    }


def transform_endorsement(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    return {**base_operation, **{
        'delegate': metadata.get('delegate'),
        'public_key': content.get('public_key'),
        'slots': metadata.get('slots')
    }}


def transform_transaction(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    operation_result = metadata.get('operation_result', EMPTY_OBJECT)
    return {**base_operation, **{
        'source': content.get('source'),
        'destination': content.get('destination'),
        'fee': safe_int(content.get('fee')),
        'amount': safe_int(content.get('amount')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'status': metadata.get('operation_result', EMPTY_OBJECT).get('status'),
        'consumed_gas': safe_int(operation_result.get('consumed_gas')),
        'storage_size': safe_int(operation_result.get('storage_size')),
    }}


def transform_delegation(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    operation_result = metadata.get('operation_result', EMPTY_OBJECT)
    return {**base_operation, **{
        'source': content.get('source'),
        'delegate': content.get('delegate'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'status': operation_result.get('status'),
    }}


def transform_reveal(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    operation_result = metadata.get('operation_result', EMPTY_OBJECT)
    return {**base_operation, **{
        'source': content.get('source'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'public_key': content.get('public_key'),
        'status': operation_result.get('status'),
    }}


def transform_seed_nonce_revelation(content, base_operation):
    return {**base_operation, **{
        'nonce': content.get('nonce')
    }}


def transform_activate_account(content, base_operation):
    return {**base_operation, **{
        'public_key_hash': content.get('pkh'),
        'secret': content.get('secret')
    }}


def transform_origination(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    operation_result = metadata.get('operation_result', EMPTY_OBJECT)
    return {**base_operation, **{
        'source': content.get('source'),
        'delegate': content.get('delegate'),
        'manager_public_key': content.get('managerPubkey'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'balance': safe_int(content.get('balance')),
        'status': content.get('metadata').get('operation_result').get('status'),
        'originated_contracts': operation_result.get('originated_contracts'),
    }}


def transform_proposals(content, base_operation):
    return {**base_operation, **{
        'source': content.get('source'),
        'proposals': content.get('proposals'),
        'period': content.get('period'),
    }}


def transform_double_baking_evidence(content, base_operation):
    bh1 = content.get('bh1', EMPTY_OBJECT)
    bh2 = content.get('bh2', EMPTY_OBJECT)
    return {**base_operation, **{
        'denounced_1_level': bh1.get('level'),
        'denounced_1_proto': bh1.get('proto'),
        'denounced_1_predecessor': bh1.get('predecessor'),
        'denounced_1_timestamp': convert_timestr_to_timestamp(bh1.get('timestamp')),
        'denounced_1_validation_pass': bh1.get('validation_pass'),
        'denounced_1_operations_hash': bh1.get('operations_hash'),
        'denounced_1_fitness': bh1.get('fitness'),
        'denounced_1_context': bh1.get('context'),
        'denounced_1_priority': bh1.get('priority'),
        'denounced_1_proof_of_work_nonce': bh1.get('proof_of_work_nonce'),
        'denounced_1_signature': bh1.get('signature'),
        'denounced_2_level': bh2.get('level'),
        'denounced_2_proto': bh2.get('proto'),
        'denounced_2_predecessor': bh2.get('predecessor'),
        'denounced_2_timestamp': convert_timestr_to_timestamp(bh2.get('timestamp')),
        'denounced_2_validation_pass': bh2.get('validation_pass'),
        'denounced_2_operations_hash': bh2.get('operations_hash'),
        'denounced_2_fitness': bh2.get('fitness'),
        'denounced_2_context': bh2.get('context'),
        'denounced_2_priority': bh2.get('priority'),
        'denounced_2_proof_of_work_nonce': bh2.get('proof_of_work_nonce'),
        'denounced_2_signature': bh2.get('signature'),
    }}


def transform_double_endorsement_evidence(content, base_operation):
    op1 = content.get('op1', EMPTY_OBJECT)
    op2 = content.get('op2', EMPTY_OBJECT)
    return {**base_operation, **{
        'denounced_1_branch': op1.get('branch'),
        'denounced_1_signature': op1.get('signature'),
        'denounced_1_level': op1.get('operations').get('level'),
        'denounced_2_branch': op2.get('branch'),
        'denounced_2_signature': op2.get('signature'),
        'denounced_2_level': op2.get('operations').get('level'),
    }}


def transform_ballot(content, base_operation):
    return {**base_operation, **{
        'source': content.get('source'),
        'proposal': content.get('proposal'),
        'period': content.get('period'),
        'ballot': content.get('ballot'),
    }}


EMPTY_OBJECT = {}
EMPTY_LIST = []