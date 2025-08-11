def addition(*args):
    total= sum(args)
    print(total)

num = input("Enter the numbers you want to add = ").split(",")
num = [int(n) for n in num ]
addition(*num)