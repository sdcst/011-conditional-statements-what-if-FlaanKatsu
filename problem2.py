#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

n = float(input("what is love? (must be a number)"))
if n == int(n):
    print("this number is an intager.")
elif n != int(n):
    print("this number is not an intager.")