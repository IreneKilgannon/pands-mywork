# Read in the modules
# Keep reading in modules until user enter a module name of blank

students = []


def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name:")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)


def readModules():
    modules = []
    moduleName = input("Enter first module name (blank to quit): ").strip()

    while moduleName != "":
           module = {}
           module["name"] = moduleName
           module["grade"] = int(input("Enter grade:"))
           modules.append(module)
           moduleName["name"] = input("Enter next module name (blank to quit): ").strip()
           moduleName["grade"] = input("Enter next grade:")

    return modules

doAdd(students)

doAdd(students)
print(students)