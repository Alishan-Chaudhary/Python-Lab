
fruit = ['mango', 50,'orange', 30,'lemon', 20] #mixed list
print(fruit[0])
print(fruit[2:4])
print(fruit[::-1])  

fruit_1 = [['mango', 100], ['orange', 50]] # 2d list
print(fruit_1[0][1])

subject = ['maths', 'science']
subject_code = [200, 2001]
merge = subject + subject_code # this merges te suject and suject_code variable 
print(merge)
join = "----".join(subject) # join helps to join the value sotre in list with particular strings
print(join)
index = subject.index('science') # index counts where in which place science is located
print(index)

course = ['python', 'data science', 'react','python']
time = [3,2,1]
ds_index = course.index('data science')
ds_time = time[ds_index] #here were asking in which place is data science and assinging the same place to ds_time and printing the time 
print(ds_time)
count = course.count('python') #count helps to count how many python are there in list
print(count)
course.append('javascript') #append helps to add in the last of the list
print(course)

course.append(['java' 'C'])
print(course)

last_item = course.pop() # pop take out the last data of the list
print(last_item)
print(course)
last_item1 =course.pop(-1) # This is poping last item of the list
print(last_item1)
pop = course.pop(2) # this is pooping the third item 
print(course)

course.insert(1,'llm') # Insert work same as append but append add items in last of the list and insert add wherevery you want like here i wanted to add in the second place so I have witten (1,llm)
print(course)

course.remove('python') # remove, simply help to remove the items form the list. If the same string is there in list then it will only remove the first one
print(course)

del course[1:3]  # del is deleting the items from 1 position to the second position 
print(course)


number= [1,2,3,4,5]
number_1 = [6,7,8,9]
number.extend(number_1) # Here extend is used to combine the number and number_1 and also add item by item
print(number)

numbers = [10, 20, 30 ,50]
print(min(numbers)) # This shows the minimun number in the list
print(sum(numbers)) # This sums all the items of the list 
print(max(numbers)) # This shows the maximun number in list

string = ['lion','a','b','tiger']
print(min(string)) # this shows the mininum string (string are arrange in accending order like arranged in a dictonary)
print(max(string)) # This shows the maimun string || || ||   ||

string_1 = ['Lion','a','b','tiger']
print(min(string_1)) # here this will print Lion because Lion starts from capital letter, so in a dictonary Capital letter comes first so Lion is the smallest or minumu
sort_len = sorted(string, key=len)
print(sort_len) 
sort = sorted(string_1, key=str.lower) # Here str.lower is first converting the items in the list into lower case and then sorted is sorting the list 
print(sort)

numbers.sort() # sort helps in sorting the items stored in number variable and doesn't create a new list it dirctly modifies the list
print(numbers) 
sort_1 = sorted(numbers) # sorted also does the same work as the sort but create a new list it doesn't modify the existing list 
print(sort_1)



# Tuple (tuple are also like of list but we can't change)

tuple = (1,2,3)
tuple_1 = ('a', 'b', 'c')
tuple_2 = ('a', 1, 'b', 2)
tuple_3 = (1, ['apple', 'ball'], ('a', 'b', 1), 'python', True)

courses = ('HTML', 'CSS','js', 'react')
course_1, course_2, *course_3 = courses

print(course_1)
print(course_2)
print(course_3)


# SET
courses = {'HTML', 'CSS','js', 'react','CSS'}
print(courses)

hello = courses.add('python')
print(courses)

add = ('DS', 12)
courses.update (add)
print(courses)


courses.discard('js')
print(courses)

print('python' in courses)
print('python' not in courses )

coureses_1 = {'HTML', 'CSS','js', 'react','CSS'}
courses_2 = {'HTML','CSS', 'python', 'java'}

common = coureses_1.intersection(courses_2)
print(common)
common_1 = coureses_1 & courses_2
print(common_1)

different = coureses_1 - courses_2
print(different)
different_1 = coureses_1.difference(courses_2)
print(different_1)


frozen = frozenset(course)
print(frozen)















