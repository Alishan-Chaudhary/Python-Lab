import json
import csv

with open('info.csv','r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

nested_data = {}
for row in data:
    phone = row.pop('phone')
    nested_data[phone]= row

with open('info_copy.json','w') as jsonfile:
    json.dump(nested_data,jsonfile)