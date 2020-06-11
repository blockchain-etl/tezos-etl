# Quickstart

Install Tezos ETL:

```bash
pip install tezos-etl
```

Export blocks, balance updates and operations ([Schema](schema.md), [Reference](commands.md#export_blocks)):

```bash
> tezosetl export_blocks --start-block 1 --end-block 500000 \
--provider-uri https://mainnet-tezos.giganode.io --output_dir output
```

Find all commands [here](commands.md).
