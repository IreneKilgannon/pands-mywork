# Create a program that puts 10 random numbers into a queue (list)
# Program should put put all the values in the queue
# removes numbers from the queue one at a time
# Print it and the current numbers in the queue
# end say the queue is now empty

import random

queue = []

for num in range(0, 10):
    queue.append(random.randint(1, 100))
print(f'queue is {queue}')


while len(queue)!= 0:
        current_number = queue.pop(0)
        print(f'current Number is {current_number} and the queue is {queue}')
print(f'the queue is now empty')
