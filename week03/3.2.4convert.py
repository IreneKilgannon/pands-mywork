# Take in an input in the from of -float, there may or may not be a minus sign
# Output: the absolute amount in cent.

amount = float(input("Please enter an amount: "))

absolute_amount = int(abs(amount) * 100)

print(f"That amount is cent is: {(absolute_amount)}")