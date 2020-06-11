# Quickstart

Install Tezos ETL:

```bash
pip install tezos-etl
```

Export blocks, balance updates and operations ([Schema](schema.md), [Reference](commands.md#export)):

```bash
> tezosetl export --start-block 1 --end-block 100 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output
```

Find all commands [here](commands.md).
