import json

student_data = {"9843":{'name': 'alishan','course':'python'},'9845':{'name':'ram','course':'java'},'9876':{'name':'shyam','course':'c'}}

with open('info.json','w') as file:
    json.dump(student_data,file)
    
# with open('info.josn','r') as file:
#     content = file.read()
# print(content)