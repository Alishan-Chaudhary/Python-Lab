name = input("Enter you name =")
birth_year = int(input("Enter the your birth year in A.D ="))
current_year = 2025
age = current_year - birth_year
if age >=18:
    print(f"{name},You are eligible for voting")
else:
    print(f"{name},You are[not] eligible for voting")
