import argparse
import pathlib

# Set file arugments
parser = argparse.ArgumentParser()
parser.add_argument("--file", type=pathlib.Path, default="./test.csv", help="Enter file name with directory")
parser.add_argument("--indexes", type=int, default=100, help="How many potential items can be in one collection")
parser.add_argument("--id-length", type=int, default=6, help="The maximum length an item id could be")
args = parser.parse_args()

# Set global variables
defined_path = args.file
indexes = args.indexes
id_length = args.id_length
lines_cleaned = 0
cleaned_instances = 0

# Start script
print("Starting WP Export Cleaner")
print("Cleaning: %s" % defined_path)

with open(defined_path, "r") as file:
    data = file.read()
    clean_data = data
    for index in range(indexes):
        for length in range(id_length):
            # Check for start of collection
            clean_data = clean_data.replace('a:%s:{i:0;s:%d:""' % (index, length), '')
            # Clean collection items
            clean_data = clean_data.replace('"";i:%s;s:%d:""' % (index, length), "|")
    # Remove tail
    clean_data = clean_data.replace('"";}','')

with open("output.csv", "w", encoding="utf-8") as file:
    file.write(clean_data)
    print("Written to: ./output.csv")

print("Completed")