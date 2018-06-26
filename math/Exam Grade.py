# It's a program for calculate exam grade
point = int(input("Enter your Exam point:"))

if point > 100:
    print("Wrong Input!!")
elif point >= 80:
    print("Your grade is A+")
elif point >= 70:
    print("Your grade is A")
elif point >= 60:
    print("Your grade is A-")
elif point >= 55:
    print("Your grade is B")
elif point >= 50:
    print("Your grade is C")
elif point >= 40:
    print("Your grade is D")
else:
    print("Your grade is F")
