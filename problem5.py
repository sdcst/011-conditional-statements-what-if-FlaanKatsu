#! python3

"""
In math, if a quadratic equation is in the format
ax^2 + bx + c = 0, the discriminant can be calculated as
b^2 - 4 * a * c
If the discriminant is a perfect square, the equation can
be factored.  Furthermore, if the discriminant is negative,
then the equation has no solutions (not used in this assignment).
Have the user enter in values for a, b and c and then 
tell them if the equation can be factored.

Inputs:
- 3 numbers (a, b, c)

Outputs:
- "the equation can be factored"
- "the equation can not be factored"

Example:
Enter a: 1
Enter b: 4
Enter c: 4
the equation can be factored

Enter a: 1
Enter b: 4
Enter c: 8
the equation can not be factored

"""

input("Welcome to Lord Beelzebub's factoring evaluator!")
input("This evaluator evaluates if the discriminant of \nax^2 + bx + c = 0 can be factored.")
a = float(input("Please input the value of \"a\""))
b = float(input("Please input the value of \"b\""))
c = float(input("Please input the value of \"c\""))

