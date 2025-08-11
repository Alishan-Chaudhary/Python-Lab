file_name = "Java.txt"
pythonfile = "python.txt"
with open(pythonfile,'r') as file:
    content= file.read()

change_content = content.replace("Python","Java").replace("python","java")


with open(file_name,'w') as file_obj:
    file_obj.write(change_content)

print(content)

    