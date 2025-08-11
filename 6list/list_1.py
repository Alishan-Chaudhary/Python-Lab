student_marks = [41, 41, 41, 41, 41]
scored_marks = sum(student_marks)
total_marks = 500 
grade = total_marks - scored_marks
minimum = min(student_marks)

if minimum > 40 and grade <= 50 :
    print(f"Congratulation !! You've passed in grade A+.")
elif minimum > 40 and grade <= 100:
    print(f"Congratulation !! You've passed in grade A.")
elif minimum > 40 and grade <= 150:
    print(f"Congratulation !! You've passed in grade B+.")
elif minimum > 40 and grade <= 200:
    print("Congratulation !! You've passed in grade B.") 
elif minimum > 40 and grade <= 250:
    print("Congratulation !! You've passed in grade C+.")
elif minimum > 40 and grade <=300:
    print("Congratulations !! You've passed in grade C.")
elif minimum > 40 and grade <=350:
    print("Congratulations !! You've passed in grade D+.")
else:
    print("You've failed.")
