# hash-csv
The following python utility takes a CSV file as input and hashes given columns with SHA2_256.

## Inputs
- -c --config path/to/my_config.json passed in at runtime. Example:
            
            python3 hash-csv.py --config path/to/my_config.json

- -s --source path/to/my_data.csv passed in at runtime. Example:
            
            python3 hash-csv.py --source path/to/my_data.csv

TODO:
- -a --algorithm) - to be manually added into .py script, for now. Accepted that SHA2_256 will be used.

## Config File
The config file is a JSON file that is included with this repo. Edit the text in the config/config.json file to customise for your use-case:

| Key Name   | What it does |
| ---------- | ------------ |
| hash_fields| Defines the target columns to be hashed in the CSV file (e.g. Email)|
| out_dir| Defines the directory prefix where the script will output the hashed CSV|

JSON schema and syntax constraints should be observed, otherwise the script will fail.

## Outputs
A CSV hashed according to the above inputs will be produced at the destination defined in config.