import argparse
import csv

# Set file arugments
parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str,default="./test.csv", help="Enter file name with directory")
args = parser.parse_args()

# Set global variables
defined_path = args.file
indexes = 100
id_length = 6
lines_cleaned = 0
cleaned_instances = 0

# Start script
print("Starting WP Export Cleaner")
print("Cleaning: %s" % defined_path)

# try:

with open(defined_path, "r") as file:
    data = file.read()
    clean_data = data
    # clean_data = data.replace('"";i:1;s:3:""', "|")
    for index in range(indexes):
        # clean_data = clean_data.replace
        for length in range(id_length):
            clean_data = clean_data.replace('a:%s:{i:0;s:%d:""' % (index, length), '')
            clean_data = clean_data.replace('"";i:%s;s:%d:""' % (index, length), "|")
    clean_data = clean_data.replace('"";}','')

with open("output.csv", "w", encoding="utf-8") as file:
    file.write(clean_data)
    print("Written to: ./output.csv")

print("Completed")