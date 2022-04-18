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

import json

from tezosetl.enums.operation_kinds import OperationKind
from tezosetl.utils.cast_utils import safe_int


def map_operations(block, response):
    for operation_group_index, operation_index, operation in yield_operations(response):
        for content_index, content in enumerate(operation.get('contents', EMPTY_LIST)):
            operation_kind = content.get('kind')

            base_operation = map_base_operation(
                block, operation_group_index, operation_index, content_index, operation, operation_kind
            )

            yield map_operation(operation_kind, content, base_operation)

            metadata = content.get('metadata', EMPTY_OBJECT)
            for index, result in enumerate(metadata.get('internal_operation_results', EMPTY_LIST)):
                base_internal_operation = {**base_operation, **{
                    'internal_operation_index': index
                }}
                internal_operation_kind = result.get('kind')
                yield map_operation(internal_operation_kind, result, base_internal_operation)


def yield_operations(response):
    for operation_group_index, operation_group in enumerate(response.get('operations', EMPTY_LIST)):
        for operation_index, operation in enumerate(operation_group):
            yield operation_group_index, operation_index, operation


def map_base_operation(block, operation_group_index, operation_index, content_index, operation, operation_kind):
    return {
        'item_type': f'{operation_kind}_operation',
        'level': block.get('level'),
        'timestamp': block.get('timestamp'),
        'block_hash': block.get('block_hash'),
        'branch': operation.get('branch'),
        'signature': operation.get('signature'),
        'operation_hash': operation.get('hash'),
        'operation_group_index': operation_group_index,
        'operation_index': operation_index,
        'content_index': content_index,
        'internal_operation_index': None,
    }


def map_operation(operation_kind, content, base_operation):
    if operation_kind == OperationKind.endorsement:
        return map_endorsement(content, base_operation)
    elif operation_kind == OperationKind.preendorsement:
        return map_endorsement(content, base_operation)
    elif operation_kind == OperationKind.endorsement_with_slot:
        return map_endorsement_with_slot(content, base_operation)
    elif operation_kind == OperationKind.transaction:
        return map_transaction(content, base_operation)
    elif operation_kind == OperationKind.delegation:
        return map_delegation(content, base_operation)
    elif operation_kind == OperationKind.reveal:
        return map_reveal(content, base_operation)
    elif operation_kind == OperationKind.seed_nonce_revelation:
        return map_seed_nonce_revelation(content, base_operation)
    elif operation_kind == OperationKind.activate_account:
        return map_activate_account(content, base_operation)
    elif operation_kind == OperationKind.origination:
        return map_origination(content, base_operation)
    elif operation_kind == OperationKind.proposals:
        return map_proposals(content, base_operation)
    elif operation_kind == OperationKind.double_baking_evidence:
        return map_double_baking_evidence(content, base_operation)
    elif operation_kind == OperationKind.double_endorsement_evidence:
        return map_double_endorsement_evidence(content, base_operation)
    elif operation_kind == OperationKind.double_preendorsement_evidence:
        return map_double_endorsement_evidence(content, base_operation)
    elif operation_kind == OperationKind.set_deposits_limit:
        return map_set_deposits_limit(content, base_operation)
    elif operation_kind == OperationKind.ballot:
        return map_ballot(content, base_operation)    
    elif operation_kind == OperationKind.register_global_constant:
        return map_register_global_constant(content, base_operation)
    else:
        raise KeyError(f'Operation kind {operation_kind} not recognized. {json.dumps(content)}')


def map_endorsement(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    return {**base_operation, **{
        'delegate': metadata.get('delegate'),
        'public_key': content.get('public_key'),
        'slots': metadata.get('slots')
    }}

def map_endorsement_with_slot(content, base_operation):
    metadata = content.get('metadata', EMPTY_OBJECT)
    endorsement = content.get('endorsement', EMPTY_OBJECT)
    operations = endorsement.get('operations', EMPTY_OBJECT)
    return {**base_operation, **{
        'delegate': metadata.get('delegate'),
        'endorsement_branch': endorsement.get('branch'),
        'endorsement_signature': endorsement.get('signature'),
        'operations_kind': operations.get('kind'),
        'operations_level': operations.get('level'),
        'slot': content.get('slot'),
        'slots': metadata.get('slots')
    }}

def map_set_deposits_limit(content, base_operation):
    operation_result = get_operation_result(content)

    return {**base_operation, **{
        'source': content.get('source'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'limit': safe_int(content.get('limit')),
        'status': operation_result.get('status'),
        'consumed_gas': safe_int(operation_result.get('consumed_gas'))
    }}

def map_transaction(content, base_operation):
    operation_result = get_operation_result(content)

    return {**base_operation, **{
        'source': content.get('source'),
        'destination': content.get('destination'),
        'fee': safe_int(content.get('fee')),
        'amount': safe_int(content.get('amount')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'status': operation_result.get('status'),
        'consumed_gas': safe_int(operation_result.get('consumed_gas')),
        'storage_size': safe_int(operation_result.get('storage_size')),
        'parameters': json_dumps(content.get('parameters')),
    }}


def map_delegation(content, base_operation):
    operation_result = get_operation_result(content)

    return {**base_operation, **{
        'source': content.get('source'),
        'delegate': content.get('delegate'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'status': operation_result.get('status'),
    }}

def map_register_global_constant(content, base_operation):
    operation_result = get_operation_result(content)

    return {**base_operation, **{
        'source': content.get('source'),
        'destination': content.get('destination'),
        'fee': safe_int(content.get('fee')),
        'amount': safe_int(content.get('amount')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'status': operation_result.get('status'),
        'consumed_gas': safe_int(operation_result.get('consumed_gas')),
        'storage_size': safe_int(operation_result.get('storage_size')),
        'value': json_dumps(content.get('value')),
    }}

def map_reveal(content, base_operation):
    operation_result = get_operation_result(content)

    return {**base_operation, **{
        'source': content.get('source'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'public_key': content.get('public_key'),
        'status': operation_result.get('status'),
    }}


def map_seed_nonce_revelation(content, base_operation):
    return {**base_operation, **{
        'nonce': content.get('nonce')
    }}


def map_activate_account(content, base_operation):
    return {**base_operation, **{
        'public_key_hash': content.get('pkh'),
        'secret': content.get('secret')
    }}


def map_origination(content, base_operation):
    operation_result = get_operation_result(content)

    return {**base_operation, **{
        'source': content.get('source'),
        'delegate': content.get('delegate'),
        'manager_public_key': content.get('managerPubkey'),
        'fee': safe_int(content.get('fee')),
        'counter': safe_int(content.get('counter')),
        'gas_limit': safe_int(content.get('gas_limit')),
        'storage_limit': safe_int(content.get('storage_limit')),
        'balance': safe_int(content.get('balance')),
        'status': operation_result.get('status'),
        'originated_contracts': operation_result.get('originated_contracts'),
        'script': json_dumps(content.get('script')),
    }}


def map_proposals(content, base_operation):
    return {**base_operation, **{
        'source': content.get('source'),
        'proposals': content.get('proposals'),
        'period': content.get('period'),
    }}


def map_double_baking_evidence(content, base_operation):
    bh1 = content.get('bh1', EMPTY_OBJECT)
    bh2 = content.get('bh2', EMPTY_OBJECT)
    return {**base_operation, **{
        'denounced_1_level': bh1.get('level'),
        'denounced_1_proto': bh1.get('proto'),
        'denounced_1_predecessor': bh1.get('predecessor'),
        'denounced_1_timestamp': bh1.get('timestamp'),
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
        'denounced_2_timestamp': bh2.get('timestamp'),
        'denounced_2_validation_pass': bh2.get('validation_pass'),
        'denounced_2_operations_hash': bh2.get('operations_hash'),
        'denounced_2_fitness': bh2.get('fitness'),
        'denounced_2_context': bh2.get('context'),
        'denounced_2_priority': bh2.get('priority'),
        'denounced_2_proof_of_work_nonce': bh2.get('proof_of_work_nonce'),
        'denounced_2_signature': bh2.get('signature'),
    }}


def map_double_endorsement_evidence(content, base_operation):
    op1 = content.get('op1', EMPTY_OBJECT)
    op2 = content.get('op2', EMPTY_OBJECT)
    return {**base_operation, **{
        'denounced_1_branch': op1.get('branch'),
        'denounced_1_signature': op1.get('signature'),
        'denounced_1_level': op1.get('operations', EMPTY_OBJECT).get('level'),
        'denounced_2_branch': op2.get('branch'),
        'denounced_2_signature': op2.get('signature'),
        'denounced_2_level': op2.get('operations', EMPTY_OBJECT).get('level'),
    }}


def map_ballot(content, base_operation):
    return {**base_operation, **{
        'source': content.get('source'),
        'proposal': content.get('proposal'),
        'period': content.get('period'),
        'ballot': content.get('ballot'),
    }}


def get_operation_result(content):
    metadata = content.get('metadata', EMPTY_OBJECT)
    if metadata.get('operation_result') is not None:
        return metadata.get('operation_result')
    elif content.get('result') is not None:
        return content.get('result')
    else:
        return EMPTY_OBJECT


def json_dumps(obj):
    if obj is None:
        return None
    return json.dumps(obj, separators=(',', ':'))


EMPTY_OBJECT = {}
EMPTY_LIST = []
