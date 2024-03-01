# Write a function that prints out a menu of commands that we can perform
#The function should return what the user chose

#choices = input("What would you like to do?\n\t(a) Add new student\n\t(v) View students\n\t(q) Quit\nType one letter (a/v/q):")

#print(f"you chose {choices}")

def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
choice = menu()
print(f"you chose {choice}")

