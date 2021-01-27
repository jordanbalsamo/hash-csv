# hash_csv
hash_csv takes a given CSV file as input and outputs a SHA2_256 hashed CSV. You have full control over the desired columns to be hashed via config 👍.

## Intall

hash_csv can be installed and setup by running:
```
$ python -m venv .venv              # create a virtual env
$ source .venv/bin/activate         # activate your virtual env
$ pip install -r requirements.txt   # install hash_csv dependencies
```

## Usage

hash_csv can be invoked from the commandline with the following:
```
$ python hash_csv.py --source path/to/source.csv --config path/to/config.json
```

## Inputs
See below for an idea of how to pass arguments to the script via the CLI:

```
- --config # Example: $ python3 hash_csv.py --config path/to/my_config.json

- --source # Example: $ python3 hash_csv.py --source path/to/my_data.csv
```

## Config File
The config file is a JSON file that is included with this repo. Edit the text in the config/config.json file to customise for your use-case:

| Key Name    | What it does |
| ----------  | ------------ |
| `hash_fields` | Defines the target columns to be hashed in the CSV file (e.g. Email)     |
| `out_dir`     | Defines the directory prefix where the script will output the hashed CSV |

JSON schema and syntax constraints should be observed, otherwise the script will fail.

## Outputs
A CSV hashed according to the above inputs will be produced at the destination defined in config.

## Contributing and TODO
To contribute to this project, raise a pull request! Check out the issues and project for inspiration.
