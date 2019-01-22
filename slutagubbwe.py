import argparse 
import csv
with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'], row['email'])
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str ,help="random text här")
args = parser.parse_args()
print(args.file)