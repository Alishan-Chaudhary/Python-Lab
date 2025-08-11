name = input("Enter your name = ")
time = int(input("Enter time = "))
if time < 0 or time > 23:
    print("invalid time")
elif time >= 5 and time <= 12:
    print(f"Good Morning {name}")
elif time > 12 and time <= 17:  
    print(f"Good Afternoon {name}")
elif time > 17 and time <= 20:
    print(f"Good Evening {name}")
elif time <= 4 or time >  20:
    print(f"Good Night {name}")
