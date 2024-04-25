#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

import math
n = float(input("please enter a number: "))
nn = n / 2
na = math.floor(nn)
nb = math.ceil(nn)
if n != int(n):
    print("Error: please enter an intager.")
else:
    if na == nb:
        print(f"the number \"{int(n)}\" is an even number.")
    else:
        print(f"the number \"{int(n)}\" is an odd number.")