# tezos-etl

JSON RPC docs: https://tezos.gitlab.io/developer/rpc.html

Operation types:

```bash
./tezos-client rpc schema post /chains/main/blocks/head/helpers/forge/operations | jq '.input.definitions."operation.alpha.contents".oneOf | .[] | .properties.kind.enum | .[0]'
```

blocks
balance_updates

operations_activate_account
operations_ballot
operations_delegation
operations_double_baking_evidence
operations_double_endorsement_evidence
operations_endorsement
operations_origination
operations_proposals
operations_reveal
operations_seed_nonce_revelation
operations_transaction

operations - a view that combines data from operations_* tables above. Only common fields are in this view.