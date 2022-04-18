class OperationKind:
    activate_account = 'activate_account'
    ballot = 'ballot'
    delegation = 'delegation'
    double_baking_evidence = 'double_baking_evidence'
    double_endorsement_evidence = 'double_endorsement_evidence'
    double_preendorsement_evidence = 'double_preendorsement_evidence'
    endorsement = 'endorsement'
    preendorsement = 'preendorsement'
    endorsement_with_slot = 'endorsement_with_slot'
    origination = 'origination'
    proposals = 'proposals'
    register_global_constant = 'register_global_constant'
    reveal = 'reveal'
    seed_nonce_revelation = 'seed_nonce_revelation'
    set_deposits_limit = 'set_deposits_limit'
    transaction = 'transaction'

    ALL = [
        activate_account,
        ballot,
        delegation,
        double_baking_evidence,
        double_endorsement_evidence,
        double_preendorsement_evidence,
        endorsement,
        preendorsement,
        endorsement_with_slot,
        origination,
        proposals,
        register_global_constant,
        reveal,
        seed_nonce_revelation,
        set_deposits_limit,
        transaction,
    ]
