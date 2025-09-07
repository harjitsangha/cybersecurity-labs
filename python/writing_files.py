# python writing files (.txt, .json, .csv)

employees = ["Eugene", "Squidward", "Spogebob", "Patrick"]
txt_data = "I like pizza!"
file_path = "employees.txt"



# txt 
try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("File already exits!")

# json

import json

staff_data = "staff.json"
staff = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

try:
    with open(staff_data, "w") as file:
        json.dump(staff, file, indent=4)
        print(f"json file '{file_path}' was created")

except FileExistsError:
    print("File already exits!")

# csv

import csv

file_path = "workers.csv"

workers = [["Name", "Age", "Job"],
           ["Spongebob", 30, "Cook"],
           ["Sandy", 27, "Scientist"],
           []
]

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in workers:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("File already exits!")