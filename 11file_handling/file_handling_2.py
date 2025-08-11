file_path = "python.txt"
add_txt = ''' I will learn Error Handling Next.'''

file_obj = open(file_path,'a')
file_obj.write(add_txt)
file_obj.close()