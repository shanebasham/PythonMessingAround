
grade = int(input("What is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit <= 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""

if letter == "F":
    sign = ""

print(f"Your grade is: {letter}{sign}")

if grade >= 70:
    print("You passed!")
else:
    print("You failed, try again!")