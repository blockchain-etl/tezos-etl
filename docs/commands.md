# Commands

All the commands accept `-h` parameter for help, e.g.:

```bash
> tezosetl export_blocks -h

Usage: tezosetl export_blocks [OPTIONS]

  Export blocks and transactions.

Options:
  -s, --start-block INTEGER   Start block
  -e, --end-block INTEGER     End block  [required]
  -p, --provider-uri TEXT     The URI of the provider e.g. https://mainnet-tezos.giganode.io
  -w, --max-workers INTEGER   The maximum number of workers.
  --output-dir TEXT        The output dir for block data.
  -h, --help                  Show this message and exit.
```

For the `--output` parameters the supported types are csv and json. The format type is inferred from the output file name.

#### export_blocks

```bash
> tezosetl export_blocks --start-block 0 --end-block 500000 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output 
```

Omit `--blocks-output` or `--transactions-output` options if you want to export only transactions/blocks.

You can tune `--batch-size`, `--max-workers` for performance.

[Blocks and transactions schema](schema.md#blockscsv).


#### get_block_range_for_date

```bash
> tezosetl get_block_range_for_date --provider-uri=https://mainnet-tezos.giganode.io --date 2020-01-01
760512,761937
```