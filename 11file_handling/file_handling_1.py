file_path = "python.txt"

file_content = '''
Python is a popular, high-level programming language known for its simplicity and readability.
It is widely used in web development, data science, artificial intelligence, and automation.
Python's clean syntax makes it easy for beginners to learn and use.
It has a large community and many libraries that support different applications.
Overall, Python is a versatile and powerful tool for modern programming.
'''

file_obj = open(file_path,'w')
file_obj.write(file_content)
file_obj.close()