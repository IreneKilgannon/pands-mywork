#Program that reads in a string, strips any leading or trailing space and convert string to lower case
# Thoughts strip(), lower()

message = input("Please enter a string: ")

#remove leading or trailing space

strip_message = message.strip()

# comvert to lower case
lower_message = strip_message.lower()

print(f"That string normalised is:{lower_message} \nwe reduced the input string from {len(message)} to {len(lower_message)}.")


#Better way
# normalised_string = message.strip().lower()