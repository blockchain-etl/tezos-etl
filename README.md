# tezos-etl

JSON RPC docs: https://tezos.gitlab.io/developer/rpc.html

Public Tezos node: https://tezos.giganode.io/#startUsing

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
./tezos-client rpc schema post /chains/main/blocks/head/helpers/forge/operations | jq '.input.definitions."operation.alpha.contents".oneOf | .[] | .properties.kind.enum | .[0]'
```
