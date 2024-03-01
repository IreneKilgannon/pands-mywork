# doAdd() function
# Read in student name
# Read in the moudle names and grades
# Test the function, it creates a student dict
# Add student dict to list
# Test this

students = []


def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name:")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    return[]

doAdd(students)

doAdd(students)
print(students)