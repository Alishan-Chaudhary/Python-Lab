# To read a file
# file_path = "file_txt.doc"

# file_obj = open(file_path,"r")
# file_content = file_obj.read()
# file_obj.close()
# print(file_content)

# To write in a file
# file_path = "newfile.doc"
# newfile_content = '''
# this is new file to write in 
# this using python
# '''

# file_obj = open(file_path,'w')
# file_obj.write(newfile_content)
# file_obj.close()

# # to append in a file
# file_path = "newfile.doc"
# newfile_content = '''
# end
# '''

# file_obj = open(file_path,'a')
# file_obj.write(newfile_content)
# file_obj.close()

# To read line by line
file_path = "newfile.doc"
newfile_content = '''
end
'''

file_obj = open(file_path,'r')
for line in file_obj.readlines():
    print(line)
file_obj.close()