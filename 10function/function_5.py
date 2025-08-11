def prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
           return False
    return True
number =int(input("Enter a number = "))
print(prime(number))



count = 1
num = 1
while count <= 15:
    if prime(num):
        print(num)
        count = count+1
        num = num+1
    num = num + 1
     
