import csv
import hashlib
import getopt, sys, os

# OPTIONS (Need to be paramterised):

HASH_FIELDS = ['customer_name', 'customer_gender', 'customer_dob']

CSV_FILE_NAME = ""
CSV_FILE_ENCODING = "ISO-8859-1"

CURRENT_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
OUTPUT_DIR = 'hash-csv-output'


def cmdArgument(argv):
    """
    Parses command line arguments
    Calls checkArguments to validate
    :rtype : string
    :return: name
    """
    sourceFile = "" 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:s:", ["help","source"])
    except getopt.GetoptError:
        print (help())
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print (help())
            sys.exit()
        elif opt in ("-s", "--source"):
            sourceFile = arg
    return sourceFile

def help():
    """
    Help section
    :return: Instructions string
    """
    Instructions = """\n
    Script to obfuscate CSV files using hashlib SHA-256 library

    -s, --source                     Source File Name                  
    
    Examples:
    python hash-csv.py -s "my-sensitive-file"
    
    Dependencies (can be installed via pip):
    csv
    hashlib
    getopt, sys, os

    For any other questions, speak to Jordan.

    """
    return Instructions

def main():
    
    print('\nHashing task has begun...\n')
   
    fileNameInput = CSV_FILE_NAME
    fileNameOutput = '{0}-obfuscated'.format(fileNameInput)
    fileInputPath = '{0}\\{1}.csv'.format(CURRENT_DIR,fileNameInput)
    fileOutputPath = '{0}\\{1}\\{2}.csv'.format(CURRENT_DIR,OUTPUT_DIR,fileNameOutput)
    
    try:
        with open(fileOutputPath, 'w', encoding=CSV_FILE_ENCODING, newline='\n') as outFile:

            fileWriter = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            with open(fileInputPath, encoding=CSV_FILE_ENCODING, newline='') as inFile:
            
                reader = csv.DictReader(inFile)                
                headers = next(reader)
                
                #Confirm input arguments and targets:
                print('\n HASHED FIELDS: {0}\n'.format(HASH_FIELDS))
                print(str(headers.keys()))
                
                # Headers:
               
                print(headers)

                fileWriter.writerow(headers)

                # Write first values from first row.

                firstValues = list(
                    map(
                        lambda hk, hv: hv if hk not in HASH_FIELDS else hashlib.sha256((hv).encode('utf-8')).hexdigest(),
                        headers.keys(), headers.values()
                        )
                    )

                fileWriter.writerow(firstValues)
                
                # Rest of file:
                for index, row in enumerate(reader):
                    for c in headers:
                        row[c] = row[c] if c not in HASH_FIELDS else hashlib.sha256((row[c]).encode('utf-8')).hexdigest()
                    
                    fileWriter.writerow(row.values())
                                    
                print('\nHashing task completed successfully.')
                print('\nYour hashed file has been saved to: \n\t{0}\\{1}\\{2}-obfuscated.csv \n'.format(CURRENT_DIR, OUTPUT_DIR, CSV_FILE_NAME))

    except (FileNotFoundError, IOError) as e:
        print('Hashing task failed!\n')
        print('Likely that the CMD arg you passed in did not match a file in the current directory. \n\n Current Directory: \n\t{0} \n\n System Generated Error: \n\t{1}\n'.format(CURRENT_DIR, e) )



if __name__ == '__main__':
    if os.path.isdir('{0}\\{1}'.format(CURRENT_DIR, OUTPUT_DIR)) != True:
        print('\nNew {1} directory created at: {0}\\{1}\n\n'.format(CURRENT_DIR, OUTPUT_DIR))
        os.mkdir('{0}\\{1}'.format(CURRENT_DIR, OUTPUT_DIR))
    print('\nNOTE: hash-csv.py should reside in the same directory as the file declared via CMD args (-s/--source). It will output to /{0} in the same directory\n'.format(OUTPUT_DIR))
    CSV_FILE_NAME = cmdArgument(sys.argv[1:])
    main()