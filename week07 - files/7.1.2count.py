# Write a program that counts how many times it was run


# Create a file.
'''with open("count.txt", "w") as f:
    data = f.write("0")
    print(data)
'''
    

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

num = readNumber()
num +=1
print(f"We have run this program {num} times")
writeNumber(num)