# reading files = .txt, .json, .csv

# txt file
file_path = "output.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()

    print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to read this file.")

# json

import json
file_path = "staff.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
    print(content["name"])
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to read this file.")

# csv
import csv
file_path = "workers.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to read this file.")
