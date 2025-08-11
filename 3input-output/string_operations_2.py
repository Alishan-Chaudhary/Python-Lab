"""Take an string as input from user and convert it into title case"""

variable = input("Enter a variable =")
in_title = variable.title()
print(f"your name in title case is {in_title}")


"""Take input from user and find the reverse of string provided"""
name = input("Enter you name =")
reverse = name[::-1]
print(f"Reversed of your name is {reverse}")


"""Ask the user for the file and check if the file is python program or not """
file_name = input("Enter the name of the file = ")
check = file_name.endswith(".py")
print(f"{check}")


"""Ask the user for a fruit name and replace it with orange """

fruit_name = input("Enter  a fruit name =")
replace = fruit_name.replace(fruit_name, "oranges")
print(f"Your {fruit_name} is replaced to {replace} ")


"""Ask the for a sentence and count the number of vowels in the sentence"""

sentence = input("Enter your sentences =")
sentence_lower = sentence.lower()
vowels = sentence_lower.count('a') + sentence_lower.count('e') + sentence_lower.count('i') + sentence_lower.count('o') + sentence_lower.count('u')
print(f"The total amount of vowels in your sentence is ={vowels}")


"""Take an input from user and check if the value stored in the string variable can be converted into numeric data type"""

variable_1 = input("Enter anything =")
check_numeric = variable_1.isnumeric()
print(check_numeric)


"""Take input from user and dispaly the fith and the last character of the string"""

character = input("Enter a word =")
diaplay = character[4], character[-1]
print(f"Fifth character of your word is {diaplay[0]}\nYour last character of your word is {diaplay[1]} ")

