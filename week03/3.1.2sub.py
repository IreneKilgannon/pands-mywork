# Program to subtract one number from another.
# input reads in a string so we need to convert it into and int
# so we can perform mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

answer = x-y
print(" {} minus {} is {}".format(x, y, answer))

# Newer more preferable way of formatting. 
print(f"{x} minus {y} is {answer}")