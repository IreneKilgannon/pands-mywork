# A program that reads in a student's percentage mark, rounds it and prints out the corresponding grade
# The program also checks that the grade percentage is valid
# Author: Irene Kilgannon


percentage = round(float(input("Please enter the percentage: ")))

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
