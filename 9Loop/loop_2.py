numbers = (1,4,7,12,17,20)

even_sum = 0

for num in numbers:
    if num % 2 == 0:
      print(num)
      even_sum = even_sum+num
        
print(even_sum)     
