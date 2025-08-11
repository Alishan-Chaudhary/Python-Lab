user_input = ['1','2','5']
total = sum(map(lambda number : float(number),user_input))
print(total)

total_1 = list(map(lambda number_1:2*float(number_1),user_input))
print(total_1)


#reduce in map
from functools import reduce

number_list = [4,6,7,8]
total_2 = reduce(lambda num_1,num_2: num_1 + num_2,number_list)
print(total_2)