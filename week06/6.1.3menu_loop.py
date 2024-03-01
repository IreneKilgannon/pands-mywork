# Create a program that keeps displaying the menu until the user picks 'q'
# If user chooses "a", then call a function called doAdd()
# If user chooses "v", then call a function called doView()
# Copied the function from the last program to this one.


def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

# Creating function doAdd()
def doAdd():
    print("in adding")


# Creating function doView()
def doView():
    print("in viewing")

choice = menu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nPlease select a, v, or q")
    choice = menu()

    menu()
