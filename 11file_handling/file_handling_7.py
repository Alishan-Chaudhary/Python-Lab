import json
import csv

with open('info.json','r') as file:
    student_data = json.load(file)

unnested_data = []
for phone,info in student_data.items():
    info['phone'] = phone 
    unnested_data.append(info)

with open('info.csv','w') as csvfile:
    filedname = ['phone','name','course']
    writer = csv.DictWriter(csvfile,fieldnames=filedname)

    writer.writeheader()
    writer.writerows(unnested_data)