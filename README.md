# Tezos ETL

[![Build Status](https://travis-ci.org/blockchain-etl/tezos-etl.png)](https://travis-ci.org/blockchain-etl/tezos-etl)
[![Documentation Status](https://readthedocs.org/projects/tezos-etl/badge/?version=latest)](https://tezos-etl.readthedocs.io/en/latest/?badge=latest)

[Full documentation available here](http://tezos-etl.readthedocs.io/).

## Quickstart

Install Tezos ETL:

```bash
pip install tezos-etl
```

Export blocks, balance updates and operations ([Schema](docs/schema.md), [Reference](docs/commands.md#export_blocks)):

```bash
> tezosetl export_blocks --start-block 1 --end-block 500000 \
--provider-uri https://mainnet-tezos.giganode.io --output_dir output
```

For the latest version, check out the repo and call 
```bash
> pip install -e .
> python tezosetl.pyo
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
