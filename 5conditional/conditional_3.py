marks = int(input("Enter the marks you have obtained ="))
if marks >= 90 and marks <=100:
    print("You have scored A")
elif marks >= 80 and marks <= 89:
    print("You have scored B")
elif marks >= 70 and marks <= 79:
    print("You have socored C")
elif marks >= 60 and marks <= 69:
    print("You have scored D")
elif marks >=40 and marks < 60:
    print("You have scored F")
elif marks < 40:
    print("You have failed")
else:
    print("Your input is wrong")


