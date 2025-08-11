def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(4))
print(is_even(3))

is_it_even = lambda numbers: numbers % 2 == 0
print(is_it_even(5))
print(is_it_even(6))

productor = lambda num_1,num_2: (num_1 *num_2,num_1/num_2)
product,division = productor(5,2)
print(product)
print(division)

# using lambda

num_tuple = (1,4,9,10)
even_number = list(filter(lambda num:num % 2 == 0 , num_tuple))
print(even_number)

name_tuple = ("alishan",'aashish','bibesh')
name_n = tuple(filter(lambda name: name.lower().startswith('a'), name_tuple))
print(name_n)