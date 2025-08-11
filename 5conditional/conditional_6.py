string = input("Enter a string =")
palindrome = string[::-1]
if palindrome == string:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a plaindrome.")