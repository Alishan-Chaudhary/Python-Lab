balance = 1000
withdraw = int(input("Enter the amount you want to withdrawl = "))

if balance >= withdraw:
    balance = balance - withdraw
    print(f"{withdraw} withdrawn successfully. Your new balance is {balance}")

else:
    print("You have insufficient balance.")
    print(f"New Balance: {balance}")
