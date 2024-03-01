def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

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
           moduleName = input("Enter next module name (blank to quit): ").strip()
    return modules

def displayModules(modules):
    print(f"\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
    


students = []

choice = menu()
while (choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\n\nPlease select a, v, or q")
    choice = menu()
