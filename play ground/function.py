def my_calculation (num1, num2):
    total = num1 + num2
    difference = num1 - num2
    product = num1 * num1

    return total, difference, product

a = 15
b = 50

add, subtraction, multiplication = my_calculation(a,b)
ad, sub, multi = my_calculation(num1=5, num2= 10)
print(add,subtraction,multiplication)
print(ad,sub,multi)

def dispaly_num():
    def display_num2():
        num_1 = 5
        print(num_1)
    
    num_1 = 10
    print(num_1)
    display_num2()

num_1 = 15
print(num_1)
dispaly_num()


def incrementor (numb, increase_value = 1):
    increase = numb + increase_value

    return increase

# g = 5 
# h = incrementor(g,10)
# i = incrementor(g)n
# print(h)
# print(i)

j = int(input("Enter ="))
k = int(input ("Enter ="))
i = incrementor(j,k)
print(i)
