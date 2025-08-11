input = int(input("Enter a number of which you want factorial ="))
result = 1
n = 1
while n <= input:
    result = result * n
    n = n + 1
print(result)