name = input("Enter your Name = ")
age = int(input("Enter your age = "))
salary = float(input("Enter your salary = "))

if age >= 21 and salary >= 25000:
    print(f"{name} you are eligible for the loan.")
else :
    print(f"{name} you not eligible for the loan.")
