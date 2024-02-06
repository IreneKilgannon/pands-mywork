# This program should take ina float and output and int(rounded up or down)
# Caution! round, rounds to the nearest even number

roundfloat = input("Enter a float number: ")

rounded = int(float(roundfloat))

print(f'{roundfloat} rounded is {rounded}')
# error rounded2 = int(rounded)  In the above 3.5 is rounded down. Changed


#Answer in worksheet
number_to_round = float(input("Enter a float number:"))
rounded_number = round(number_to_round)
print(f"{number_to_round} rounded is {rounded_number}")

# Think about how would i get accurate rounding. 
# https://inspector.dev/how-to-round-numbers-in-python-fast-tips/#:~:text=The%20simplest%20way%20to%20round,rounded%20to%20the%20nearest%20integer.