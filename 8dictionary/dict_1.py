broadway_coureses = {'courses':['python','java'], 'duration':[3,4]}
courses = broadway_coureses.get('courses')
check = ('python' in courses)
if check == True:
    print("There is python available")
else:
    print("Not available")