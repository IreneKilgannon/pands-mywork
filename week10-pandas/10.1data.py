import pandas as pd
import numpy as np

listDAta= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]

df = pd.DataFrame(listDAta, columns= ['name', 'subject', 'grade'])

print(df.head(3))

print(df.describe())
print(type(df.describe()))

# Write to a csv
df.to_csv('grades.csv')


# Write to excel file without the index column
df.to_excel('grades.xlsx', index= False, sheet_name= 'data')

# Add the description to another sheet called 'summary'

with pd.ExcelWriter('grades.xlsx', engine= 'openpyxl', mode= 'a') as writer:
    df.describe().to_excel(writer, sheet_name= 'summary')

# Calculate and print the mean of the grade column

print(df['grade'].mean())

# Alternative method
mean = df.describe().loc['mean','grade']
print(mean)