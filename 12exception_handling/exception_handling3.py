import csv
import json
import datetime as dt
from exception_handling_2 import user_age
from exception_handling_1 import can_drink

headers = ["Name","DOB","Mobile_Number"]
details = [
    ['Ram','2010-11-10',9848],
    ['Shyam','2001-06-15',9845]
    ]
with open('employee_info.csv','w',newline="") as file:
    file_content = csv.writer(file)

    file_content.writerow(headers)
    file_content.writerows(details)

with open('employee_info.csv','r') as csvfile:
    file_content = list(csv.DictReader(csvfile))





drink_count = {"hard_drink":0, "soft_drink":0}

for row in file_content:
    dob = row["DOB"]
    age = user_age(dob)
    if can_drink(age):
        drink_count["hard_drink"] += 1
    else:
        drink_count["soft_drink"] += 1



with open("drink_counts.json",'w') as jsonfile:
     json.dump(drink_count,jsonfile)