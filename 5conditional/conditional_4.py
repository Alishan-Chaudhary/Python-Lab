first_number = int(input("Enter the first number ="))
second_number = int(input("Enter the second number ="))
if first_number > second_number:
    print(f"{first_number} is the largest number")
elif second_number > first_number:
    print(f"{second_number} is the largest number")
else:
    print("Both number are equal")

