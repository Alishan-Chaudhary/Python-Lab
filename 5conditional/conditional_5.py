side_1 = input("Enter the length of first side of the tirangle =")
side_2 = input("Enter the lenght of second side of the tirangle =")
side_3 = input("Enter the lenght of third side of the triangle =")
if side_1 == side_2==side_3:
    print("The triangle is equliteral triangle.")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("The triangle is isosceles triangle.")
else:
    print("The triange is scalene triangle.")
    