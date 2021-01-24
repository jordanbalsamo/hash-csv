import click
import csv
import hashlib
import json
import os


def hash_csv(source, cfg):
    print(f'Hashing has started on {source} 👷.')
    
    output_file = get_file_name(source)
    output_path = f"{cfg['out_dir']}{output_file}-obfuscated.csv"    
    hash_fields = cfg['hash_fields']

    try:
        with open(output_path, 'w', encoding='ISO-8859-1', newline='\n') as out_file:

            file_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            with open(source, encoding='ISO-8859-1', newline='') as in_file:
            
                reader = csv.DictReader(in_file)                
                headers = next(reader)
                
                #Confirm input arguments and targets:
                print(f'\nHASHED FIELDS: {hash_fields}.')
                #print(str(headers.keys()))
                
                # Headers:
                file_writer.writerow(headers)

                # Write first values from first row.
                first_values = list(
                    map(
                        lambda hk, hv: hv if hk not in hash_fields else hashlib.sha256((hv).encode('utf-8')).hexdigest(),
                        headers.keys(), headers.values()
                        )
                    )

                file_writer.writerow(first_values)
                
                # Rest of file:
                for index, row in enumerate(reader):
                    for c in headers:
                        row[c] = row[c] if c not in hash_fields else hashlib.sha256((row[c]).encode('utf-8')).hexdigest()
                    
                    file_writer.writerow(row.values())
                                    
                print('\nHashing task completed successfully 💪.')

    except (FileNotFoundError, IOError) as e:
        print('Hashing task failed!\n', e)


def load_config(config):
    with open(config) as f:
        cfg = json.load(f)
    print('Config loaded 🚀!')
    return cfg


def get_file_name(path):
    file = path.split('/')[-1]
    remove_file_type = (file.split('.')[0])   
    return remove_file_type


@click.command()
@click.option('--source')
@click.option('--config')
def main(source, config):
    if not os.path.isfile(config):
        print('Invalid config file specified.')
        # Return non-zero exit code for CI integration
        exit(1)
    cfg = load_config(config)
    if not os.path.isfile(source):
        print('Invalid source file specified.')
        # Return non-zero exit code for CI integration
        exit(1)
    if not os.path.isdir(cfg['out_dir']):
        os.mkdir(cfg['out_dir'])
    #print(json.dumps(cfg, indent=4, sort_keys=True))
    hash_csv(source, cfg)

  
if __name__ == '__main__':
    main()