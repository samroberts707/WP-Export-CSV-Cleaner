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
    reader = csv.reader(file, delimiter="\t")
    cleaned_data = ""
    for line in reader:
        for index in range(indexes):
            for length in range(id_length): 
                # print("Checking id length of %s in index %d" % (length,index))
                line.replace(""";i:1;s:3:""", "|")
        cleaned_data = ''.join(line)
        lines_cleaned += 1

output = open('output.csv', "w")
output.writelines(cleaned_data)
output.close

print("Completed")
print("Lines cleaned: ", lines_cleaned)
# except:
#     print("Failed loading file")
#     exit(1)