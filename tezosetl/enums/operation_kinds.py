class OperationKind:
    activate_account = 'activate_account'
    ballot = 'ballot'
    delegation = 'delegation'
    double_baking_evidence = 'double_baking_evidence'
    double_endorsement_evidence = 'double_endorsement_evidence'
    endorsement = 'endorsement'
    endorsement_with_slot = 'endorsement_with_slot'
    origination = 'origination'
    proposals = 'proposals'
    reveal = 'reveal'
    seed_nonce_revelation = 'seed_nonce_revelation'
    transaction = 'transaction'

    ALL = [
        activate_account,
        ballot,
        delegation,
        double_baking_evidence,
        double_endorsement_evidence,
        endorsement,
        endorsement_with_slot,
        origination,
        proposals,
        reveal,
        seed_nonce_revelation,
        transaction,
    ]
