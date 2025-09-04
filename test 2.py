#this is going to be another test
#Here i am going to make a basic grade input and what letter grade it is

grade = int(input("Enter your grade (0-100): "))

running = True
while running:
    if grade >= 90:
        letter_grade = 'A'
        running = False
    elif grade >= 80:
        letter_grade = 'B'
        running = False
    elif grade >= 70:
        letter_grade = 'C'
        running = False
    elif grade >= 60:
        letter_grade = 'D'
        running = False
    elif grade >= 0:
        letter_grade = 'F'
        running = False
    else:
        grade = int(input("Invalid grade. Please enter a grade between 0 and 100: "))

print(f"Your letter grade is: {letter_grade}")
