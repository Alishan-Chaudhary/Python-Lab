import csv
file_path = "csvfile.csv"
# csvfile_content = [
#     ['name','gmail'],
#     ['alishan','alishanchaudhary00@gmail.com'],
#     ['aalu','aalu@gmail.com']
# ]

# with open(file_path,'w',newline='') as file_obj:
#     csv_write = csv.writer(file_obj)
#     csv_write.writerows(csvfile_content)

# # to read csv files
# file_path = "csvfile.csv"

with open(file_path) as file_obj:
    file_content = list(csv.reader(file_obj))

print(file_content)

# # to read csv files
# file_path = "csvfile.csv"

# with open(file_path) as file_obj:
#     file_content = list(csv.DictReader(file_obj))

# print(file_content)