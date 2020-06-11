# Commands

All commands accept `-h` parameter for help, e.g.:

```bash
> tezosetl export -h

Usage: tezosetl export [OPTIONS]

  Export blocks, balance updates and operations.

Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote Tezos node  [default:
                                  https://mainnet-tezos.giganode.io]
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -o, --output-dir TEXT           The output directory for block data.
  -h, --help                      Show this message and exit.
```

#### export

```bash
> tezosetl export --start-block 0 --end-block 500000 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output 
```

Export blocks, balance updates and operations.

You can tune `--max-workers` for performance.

[Schema](schema.md).

#### export_partitioned

```bash
> tezosetl export_partitioned --start 2018-06-30 --end 2018-06-31 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output 
```

Export blocks, balance updates and operations partitioned by date.

[Schema](schema.md).

#### get_block_range_for_date

```bash
> tezosetl get_block_range_for_date --provider-uri=https://mainnet-tezos.giganode.io --date 2020-01-01
760512,761937
```

Retrieves the block range for a given date.