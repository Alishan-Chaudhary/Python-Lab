record_of_students = {'9843':{'course':'python', 'name':'abc','present':True}, '984':{'course':'C', 'name':'efg', 'present':False}, '9874':{'course':'python', 'name':'hij', 'present': False}}
for mobile_num, info in record_of_students.items():
    if  info['course'] == 'python' and not info['present']:
        print(info['name'],"is absent.")
    # else:
    #     print(info['name'],"is present.")