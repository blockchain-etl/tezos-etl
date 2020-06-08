# Tezos ETL

[![Build Status](https://travis-ci.org/blockchain-etl/tezos-etl.png)](https://travis-ci.org/blockchain-etl/tezos-etl)

Install Tezos ETL:

```bash
pip install tezos-etl
```

Export blocks, transactions and actions ([Schema](#schema), [Reference](#export_blocks)):

```bash
> tezosetl export_blocks --start-block 1 --end-block 500000 \
--provider-uri https://mainnet-tezos.giganode.io \
--blocks-output blocks.json --transactions-output transactions.json --actions-output actions.json
```

Stream blockchain data continually to console:

```bash
> pip install tezos-etl[streaming]
> tezosetl stream -p https://mainnet-tezos.giganode.io --start-block 500000
```

For the latest version, check out the repo and call 
```bash
> pip install -e .
> python tezosetl.py
```

### Running Tests

```bash
> pip install -e .[dev]
> echo "TEZOSETL_PROVIDER_URI variable is optional"
> export TEZOSETL_PROVIDER_URI=https://mainnet-tezos.giganode.io
> pytest -vv
```

### Running Tox Tests

```bash
> pip install tox
> tox
```

---

JSON RPC docs: https://tezos.gitlab.io/developer/rpc.html

Public Tezos node: https://tezos.giganode.io/#startUsing

Get rpc list:

```bash
tezos-client -S -A mainnet-tezos.giganode.io -P 443 rpc list
```

Get block data:

```bash
curl -s localhost:8732/chains/main/blocks/4 > block4.json
curl --insecure https://mainnet-tezos.giganode.io/chains/main/blocks/head
```

Get block api schema:

```bash
tezos-client rpc schema get /chains/main/blocks/4
tezos-client -S -A mainnet-tezos.giganode.io -P 443 rpc schema get /chains/main/blocks/979686
```

Operation types:

```bash
tezos-client rpc schema post /chains/main/blocks/head/helpers/forge/operations | jq '.input.definitions."operation.alpha.contents".oneOf | .[] | .properties.kind.enum | .[0]'
```
