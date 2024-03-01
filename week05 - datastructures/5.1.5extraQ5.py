# Program that will read in the data
#student name
#modules
#course_name and grade for a student
# keep adding until no more students are to be added
# Print the results 


name = input("Enter student name: ")
modules = []
students = {}

students["name"] = name

courseName = input("Enter module name: ")

while courseName != "":
    module = {}
    module["courseName"] = courseName
    module["grade"] = int(input("Enter grade: "))
    modules.append(module)
    courseName = input("Enter another module: ")

     
print(f"Student: {students['name']}")
for module in modules:
      print(f"\t{module['courseName']}  \t{module['grade']}")
