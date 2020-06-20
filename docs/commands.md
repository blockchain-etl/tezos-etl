# Commands

All commands accept `-h` parameter for help, e.g.:

```bash
tezosetl export -h

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
tezosetl export --start-block 0 --end-block 100 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output 
```

Exports blocks, balance updates, and operations.

```
Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote Tezos node  [default:
                                  https://mainnet-tezos.giganode.io]
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json|csv]  The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

[Schema](schema.md)

#### export_partitioned

```bash
tezosetl export_partitioned --start 2018-06-30 --end 2018-06-31 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output 
```

Exports partitioned data for a range of blocks or dates.

```
Options:
  -s, --start TEXT                Start block/ISO date  [required]
  -e, --end TEXT                  End block/ISO date  [required]
  -b, --partition-batch-size INTEGER
                                  The number of blocks to export in partition.
                                  [default: 100]
  -p, --provider-uri TEXT         The URI of the remote Tezos node  [default:
                                  https://mainnet-tezos.giganode.io]
  -o, --output-dir TEXT           Output directory, partitioned in Hive style.
                                  [default: output]
  -f, --output-format [json|csv]  The output format.  [default: json]
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -B, --export-batch-size INTEGER
                                  The number of requests in JSON RPC batches.
                                  [default: 1]
```

[Schema](schema.md)

#### get_block_range_for_date

```bash
tezosetl get_block_range_for_date --provider-uri=https://mainnet-tezos.giganode.io --date 2020-01-01
760512,761937
```

Outputs start and end blocks for given date.

```
Options:
  -p, --provider-uri TEXT  The URI of the remote Tezos node  [default:
                           https://mainnet-tezos.giganode.io]
  -d, --date <LAMBDA>      The date e.g. 2018-01-01.  [required]
  -o, --output TEXT        The output file. If not specified stdout is used.
  -h, --help               Show this message and exit.
```
