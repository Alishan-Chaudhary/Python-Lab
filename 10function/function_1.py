def rectangle(length,breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f"Area of rectangle is {area}.")
    print(f"Perimeter of rectangel is {perimeter}")


length_1 = int(input("Enter the length of rectangle ="))
breadth_1 = int(input("Enter the breadth of rectangle ="))
rectangle(length_1,breadth_1)