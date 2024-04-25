#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""

n = float(input("please enter a number: "))
if n < 100:
    print("your number is less than 100.")
elif n == 100:
    print("your number is 100.")
else:
    print("your number is greater than 100.")
