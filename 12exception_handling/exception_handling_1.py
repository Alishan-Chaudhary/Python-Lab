def can_drink(age):
    if not (age,int):
        raise TypeError("Age must be in number!!!")
    if age < 0:
        raise ValueError("Age can't be in negative!!!")
    if age > 100:
        raise ValueError("Age can't be more than 100!!!")
    # if age < 18:
    #     return False
    # else:
    #     return True
    return age >= 18


user_age = int(input("Enter your age = "))
print(can_drink(user_age))
