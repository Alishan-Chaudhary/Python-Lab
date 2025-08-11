""" Human normal body temperature is 98.6 Fahrenheit. 
Now convert the temperaure taken from user in Fahrenheit into degree celsius."""
temperature = float(input("Enter the temperature in Fahrenheit ="))
degree_celsius = (temperature-32)/1.8
print(f"Your {temperature} Fahrenheit temperature in degree celsius is = {degree_celsius:.2f}")


"""Take principal input from user and calculate the returned amount at the 
end of 3 months when the interest rate yearly is 7.5%"""

principal = int(input("Enter your principal amount ="))
INTEREST_ANNUALY = 7.5
TIME = 0.25 #3/12
interest_anount= (principal*INTEREST_ANNUALY*TIME)/100
print(f"Your returened amount of {principal} principal at the end of 3 months is = RS{interest_anount:}")



""""Take of diameter of circle from user and calculate the area and 
perimeter of the based on diameter"""

diameter = float(input("Enter the diameter of circle ="))
radius = diameter/2
PI = 3.1416
area_of_circle = PI * radius **2
perimeter_of_circle  = 2 * PI * radius
print (f"The area of circle with diameter{diameter} is = {area_of_circle}")
print(f"Perimeter of circle with diamter {diameter} is = {[perimeter_of_circle]}")


"""Take two variable from user and swap them."""
variable_1 = input("Enter the first variable =")
variable_2 = input("Enter the second variable =")
variable_1, variable_2 = variable_2, variable_1
print(f"Your first swaped value is {variable_1}\n Your second swaped value is {variable_2}")


"""Take input from user in decimal and convert them in Binary,hex, and octal"""

decimal = int(input("Enter a number that you want to convert in binary, hex and octal ="))
in_binary = bin(decimal)
in_hex = hex(decimal)
in_octal = oct(decimal)
print(f"{decimal} in binary is {in_binary}")
print(f"{decimal} in hexadecimal is {in_hex}")
print(f"{decimal} in octal is {in_octal}")