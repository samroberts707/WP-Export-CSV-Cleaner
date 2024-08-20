import argparse
import csv

# Set file arugments
parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str,default="./test.csv", help="Enter file name with directory")
args = parser.parse_args()

# Set global variables
defined_path = args.file
lines_cleaned = 0

# Start script
print("Starting WP Export Cleaner")
print("Cleaning: %s" % defined_path)

try:
    csv_file = open(defined_path, "r")
except:
    print("Failed loading file")
    exit(1)