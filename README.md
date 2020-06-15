# Tezos ETL

[![Build Status](https://travis-ci.org/blockchain-etl/tezos-etl.png)](https://travis-ci.org/blockchain-etl/tezos-etl)
[![Documentation Status](https://readthedocs.org/projects/tezos-etl/badge/?version=latest)](https://tezos-etl.readthedocs.io/en/latest/?badge=latest)

[Full documentation available here](http://tezos-etl.readthedocs.io/).

## Quickstart

Install Tezos ETL:

```bash
pip install tezos-etl
```

Export blocks, balance updates and operations ([Schema](docs/schema.md), [Reference](docs/commands.md#export)):

```bash
tezosetl export --start-block 1 --end-block 100 \
--provider-uri https://mainnet-tezos.giganode.io --output-dir output --output-format json
```

For the latest version, checkout the repo and call
 
```bash
pip install -e .
python tezosetl.py
```

## Running Tests

```bash
pip install -e .[dev]
echo "TEZOSETL_PROVIDER_URI variable is optional"
export TEZOSETL_PROVIDER_URI=https://mainnet-tezos.giganode.io
pytest -vv
```

### Running Tox Tests

```bash
pip install tox
tox
```

## Running in Docker

1. Install Docker https://docs.docker.com/install/

2. Build a docker image:
        
        docker build -t tezos-etl:latest .
        docker image ls
        
3. Start the export using the image:

        docker run -v $HOME/output:/tezos-etl/output tezos-etl:latest export_partitioned \
        -s 2018-06-30 -e 2018-07-01 -p https://mainnet-tezos.giganode.io --output-format csv
