name = input("Enter your name =")
subject_1 = int(input("Enter the marks you obtained in maths ="))
subject_2 = int(input("Enter the marks you obtained in science ="))
subject_3 = int(input("Enter the marks you obtained in english ="))
subject_4 = int(input("Enter the marks you obtained in Computer ="))
subject_5 = int(input("Enter the marks you obtained in Social ="))
TOTAL_MARKS = 500
total_obtained_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total_obtained_marks/TOTAL_MARKS)*100

print(f"{name},you have scored {percentage}% in exam")