# make a function called Fibonacci in a module called myFunctions
# take in a number and return a list containing a fibonacci sequence of that many numbers
# if we enter 7 it would generate a list of Fibonacci sequence numbers of 7 numbers
#if user enters a number less thatn 0 we should raise a ValueError
# if user enters 0 it should return an empty list

import logging
#logging.basicConfig(level=logging.DEBUG)


def fibonacci (number):
    a = 0
    b = 1
    fibonacci_sequence = [0]
    for i in range(1, number):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    logging.debug("%d: %s", number, fibonacci_sequence)

if number == 0:
    return []
    
if number < 0:
    return ValueError

try: 
    fibonacci(-1)
except ValueError:
    pass
else:
    assert False, 'fibonacci missing ValueError'




# The testing code
if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return value for 0'
    assert fibonacci(1) == [0], 'incorrect return value for 1'
    print('all good')