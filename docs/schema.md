### blocks

```
level: INTEGER
proto: INTEGER
predecessor: STRING
timestamp: TIMESTAMP
validation_pass: INTEGER
operations_hash: STRING
fitness: STRING (REPEATED)
context: STRING
protocol: STRING
chain_id: STRING
block_hash: STRING
nonce_hash: STRING
consumed_gas: INTEGER
baker: STRING
voting_period_kind: STRING
cycle: INTEGER
cycle_position: INTEGER
voting_period: INTEGER
voting_period_position: INTEGER
expected_commitment: BOOLEAN
number_of_operation_groups: INTEGER
number_of_operations: INTEGER
```

### balance_updates

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
type: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
balance_update_index: INTEGER
status: STRING
kind: STRING
contract: STRING
change: INTEGER
delegate: STRING
category: STRING
```

### activate_account_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
public_key_hash: STRING
secret: STRING
```

### ballot_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
period: INTEGER
source: STRING
proposal: STRING
ballot: STRING
```

### delegation_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
source: STRING
delegate: STRING
fee: INTEGER
counter: INTEGER
gas_limit: INTEGER
storage_limit: INTEGER
status: STRING
```

### double_baking_evidence_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
denounced_1_level: INTEGER
denounced_1_proto: INTEGER
denounced_1_predecessor: STRING
denounced_1_timestamp: TIMESTAMP
denounced_1_validation_pass: INTEGER
denounced_1_operations_hash: STRING
denounced_1_fitness: STRING (REPEATED)
denounced_1_context: STRING
denounced_1_priority: INTEGER
denounced_1_proof_of_work_nonce: STRING
denounced_1_signature: STRING
denounced_2_level: INTEGER
denounced_2_proto: INTEGER
denounced_2_predecessor: STRING
denounced_2_timestamp: TIMESTAMP
denounced_2_validation_pass: INTEGER
denounced_2_operations_hash: STRING
denounced_2_fitness: STRING (REPEATED)
denounced_2_context: STRING
denounced_2_priority: INTEGER
denounced_2_proof_of_work_nonce: STRING
denounced_2_signature: STRING
```

### double_endorsement_evidence_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
denounced_1_branch: STRING
denounced_1_signature: STRING
denounced_1_level: INTEGER
denounced_2_branch: STRING
denounced_2_signature: STRING
denounced_2_level: INTEGER
```

### endorsement_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
delegate: STRING
public_key: STRING
slots: INTEGER (REPEATED)
```

### origination_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
source: STRING
delegate: STRING
manager_public_key: STRING
fee: INTEGER
counter: INTEGER
gas_limit: INTEGER
storage_limit: INTEGER
status: STRING
balance: INTEGER
script: STRING
originated_contracts: STRING (REPEATED)
```

### proposals_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
source: STRING
proposals: STRING (REPEATED)
period: INTEGER
```

### reveal_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
source: STRING
public_key: STRING
fee: INTEGER
counter: INTEGER
gas_limit: INTEGER
storage_limit: INTEGER
status: STRING
```

### seed_nonce_revelation_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
nonce: STRING
```

### transaction_operations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
branch: STRING
signature: STRING
operation_hash: STRING
operation_group_index: INTEGER
operation_index: INTEGER
content_index: INTEGER
internal_operation_index: INTEGER
source: STRING
destination: STRING
fee: INTEGER
amount: INTEGER
counter: INTEGER
gas_limit: INTEGER
storage_limit: INTEGER
status: STRING
consumed_gas: INTEGER
storage_size: INTEGER
parameters: STRING
```

### migrations

```
level: INTEGER
timestamp: TIMESTAMP
block_hash: STRING
kind: STRING
address: STRING
balance_change: INTEGER
```