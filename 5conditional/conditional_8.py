name = input("Enter your name = ")
birth = int(input("Enter your birth year in AD.= "))
current_year = 2025
age = current_year - birth

if age >= 18 and age <= 70:
    print(f"{name}, you are eligible for driving.")
else:
    print(f"{name}, you are not eligible for driving") 
