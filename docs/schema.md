### blocks

```
blocks (table name)
├── level: INTEGER
├── proto: INTEGER
├── predecessor: INTEGER
├── timestamp: TIMESTAMP
├── validation_pass: INTEGER
├── operations_hash: STRING
├── fitness: STRING (REPEATED)
├── context: STRING
├── protocol: STRING
├── chain_id: STRING
├── block_hash: STRING
├── nonce_hash: STRING
├── consumed_gas: INTEGER
├── baker: STRING
├── voting_period_kind: STRING
├── cycle: INTEGER
├── cycle_position: INTEGER
├── voting_period: INTEGER
├── voting_period_position: INTEGER
├── expected_commitment: BOOLEAN
├── number_of_operation_groups: INTEGER
├── number_of_operations: INTEGER
```

### balance_updates

```
balance_updates (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── type: STRING
├── operation_hash: STRING
├── kind: STRING
├── contract: STRING
├── change: INTEGER
├── delegate: STRING
├── category: STRING
```

### operations_activate_account

```
operations_activate_account (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── public_key_hash: STRING
├── secret: STRING
```

### operations_ballot

```
operations_ballot (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── period: INTEGER
├── source: STRING
├── proposal: STRING
├── ballot: STRING
```

### operations_delegation

```
operations_delegation (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── operation_address: STRING
├── source: STRING
├── delegate: STRING
├── fee: INTEGER
├── counter: INTEGER
├── gas_limit: INTEGER
├── storage_limit: INTEGER
├── status: STRING
```

### operations_double_baking_evidence

```
operations_double_baking_evidence (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── denounced_1_level: INTEGER
├── denounced_1_proto: INTEGER
├── denounced_1_predecessor: STRING
├── denounced_1_timestamp: INTEGER
├── denounced_1_validation_pass: INTEGER
├── denounced_1_operations_hash: STRING
├── denounced_1_fitness: STRING (REPEATED)
├── denounced_1_context: STRING
├── denounced_1_priority: INTEGER
├── denounced_1_proof_of_work_nonce: STRING
├── denounced_1_signature: STRING
├── denounced_2_level: INTEGER
├── denounced_2_proto: INTEGER
├── denounced_2_predecessor: STRING
├── denounced_2_timestamp: INTEGER
├── denounced_2_validation_pass: INTEGER
├── denounced_2_operations_hash: STRING
├── denounced_2_fitness: STRING (REPEATED)
├── denounced_2_context: STRING
├── denounced_2_priority: INTEGER
├── denounced_2_proof_of_work_nonce: STRING
├── denounced_2_signature: STRING
```

### operations_double_endorsement_evidence

```
operations_double_endorsement_evidence (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── denounced_1_branch: STRING
├── denounced_1_signature: STRING
├── denounced_1_level: INTEGER
├── denounced_2_branch: STRING
├── denounced_2_signature: STRING
├── denounced_2_level: INTEGER
```

### operations_endorsement

```
operations_endorsement (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── delegate: STRING
├── public_key: STRING
├── slots: INTEGER (REPEATED)
```

### operations_origination

```
operations_origination (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── operation_address: STRING
├── source: STRING
├── delegate: STRING
├── manager_public_key: STRING
├── fee: INTEGER
├── counter: INTEGER
├── gas_limit: INTEGER
├── storage_limit: INTEGER
├── status: STRING
├── balance: INTEGER
├── script_code: STRING
├── script_storage: STRING
├── originated_contracts: STRING (REPEATED)
```

### operations_proposals

```
operations_proposals (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── source: STRING
├── proposals: STRING (REPEATED)
├── period: INTEGER
```

### operations_reveal

```
operations_reveal (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── operation_address: STRING
├── source: STRING
├── public_key: STRING
├── fee: INTEGER
├── counter: INTEGER
├── gas_limit: INTEGER
├── storage_limit: INTEGER
├── status: STRING
```

### operations_seed_nonce_revelation

```
operations_seed_nonce_revelation (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── nonce: STRING
```

### operations_transaction

```
operations_transaction (table name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── operation_address: STRING
├── source: STRING
├── destination: STRING
├── fee: INTEGER
├── amount: INTEGER
├── counter: INTEGER
├── gas_limit: INTEGER
├── storage_limit: INTEGER
├── status: STRING
├── consumed_gas: INTEGER
├── storage_size: INTEGER
├── parameters: STRUCT
│   ├── entrypoint: STRING
│   ├── value: STRING
```

### operations

This is a view that combines data from `operations_*` tables above. 

```
operations (view name)
├── level: INTEGER
├── timestamp: TIMESTAMP
├── block_hash: STRING
├── branch: STRING
├── signature: STRING
├── operation_hash: STRING
├── operation_group_id: INTEGER
├── operation_id: INTEGER
├── operation_address: INTEGER
```
