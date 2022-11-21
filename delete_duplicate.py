import os
import argparse

"""
The purpose of this script is to renames 
files and directorie to make sure there 
is no spaces in filenames and no capital 
letters in directories names. 
"""

Old_Filenames = []

parser = argparse.ArgumentParser(
    description="Replace spaces with underscores."
)
parser.add_argument(
    "-path", type=str, help="Path of the directory where \
                              you want to replace whitespaces \
                              with underscores in filenames\
                              and remove capital in directories\
                              names."
)
args = parser.parse_args()
directory = args.path

try:
    for root, dirs, files in os.walk(directory):

        # Deletting ' 2.' files. 
        for name in files:
            print(name)
            filepath = root + '/' + name
            Old_Filenames.append(filepath)
            if ' 2.' in filepath:
                os.remove(filepath)
                print(filepath)

        # Creating backup filenames file. 
        with open(directory + '/old_filenames.tmp.txt', 'w') as file:
            for Old_Name in Old_Filenames:
                file.write(Old_Name + '\n')
            # Add date and time to the file.
            file.write('\n' + 'Date: ' + str(datetime.datetime.now()))
            

except TypeError:
    print("Error")

