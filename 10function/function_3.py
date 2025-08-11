def records(name,course='python'):
    print(f'Hello {name}, Welcome to {course}.')

std_name = input("Enter your name =")
std_course = input("Enter your course = ")
if std_course:
 records(std_name,std_course)
else:
 records(std_name)




