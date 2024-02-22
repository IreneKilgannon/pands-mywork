# Write a program that stores a students name and a list of courses and grades
# Print out the data

student = { 
    "name": "Mary", 
    "Modules": [
        {"course_name": "Programming", 
         "grade" : 45}, 
        {"course_name": "History", 
         "grade" : 99}
    ],
    "name": , 
    "Modules": [
        {"course_name": "Programming", 
         "grade" : }, 
        {"course_name": "History", 
         "grade" : }
    ]
    }


'''print(f'Student: {student["name"]}')
for module in student["Modules"]:
    print(f'\t{module["course_name"]}: {module["grade"]}')'''

while student["name"] != "Blank":
    print(f'Student: {student["name"]}')
    for module in student["Modules"]:
        print(f'\t{module["course_name"]}: {module["grade"]}')