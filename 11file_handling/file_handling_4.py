import os 
file_paths = ["python.txt","java.txt"]

for path in file_paths:
    file_size = os.path.getsize(path)
    in_kb = file_size/1024
    print(f'{path} is {in_kb} KB.')
    