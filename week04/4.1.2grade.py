# A program that reads in a student's percentage mark and prints our the corresponding grade
# The program also checks that the grade percentage is valid
# Author: Irene Kilgannon

grade = float(input("Please enter the percentage: "))

valid = (0 <= grade <= 100)
print (f"Grade {grade} is {valid}")

if grade <= 40:
    print("Fail")
elif grade > 40 and grade <= 49:
    print("Pass")
elif grade >= 50 and grade <= 59:
    print("Merit2")
elif grade >= 60 and grade <= 69:
    print("Merit1")
else:
    print("Distinction")

# Much tidier way given in the solution
    
percentage = float(input("Please enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit2")
elif percentage < 70:
    print("Merit1")
else:
    print("Distinction")
