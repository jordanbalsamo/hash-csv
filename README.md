# hash-csv

The following python utility takes CSV input and hashes given columns with SHA2_256.

***NOTE: for now, desired CSV should be placed in the dame directory as hash-csv.py script.***

## Inputs

- -s --source myfilename.csv passed in at runtime. Example:
            
            python hash-csv.py -s myfilename.csv

TODO:
- algorithm (-a --algorithm) - to be manually added into .py script, for now. Accepted that SHA2_256 will be used.
- headers (-h --headers) - to be manually added into .py script, for now.
- output (-o --output) - by default will output to hash-csv-output folder in same directory as script, for now.

## Outputs

A CSV hashed according to the above inputs will be produced at the following location:
    
        (DIRECTORY CONTAINING hash-csv)/hash-csv-output/myfilename-obfuscated.csv