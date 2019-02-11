#
# Project Euler - Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168
# Source: https://projecteuler.net/problem=1
# 
 
# 1st variable holding the value of the 1st multiple.
x = int(input("First multiple: "))
# 2nd variable holding the value of the 2nd multiple.
y = int(input("Second multiple: "))
# 3rd varialbe holding the value, that we wanna divide.
nValue = int(input("Enter the whole Value: "))
# 4th variable holding the sum of all the mltiples.
nSum = 0

# Error checking!
if (nValue > x and nValue > y) and (x > 1 and y > 1 and x != y):
    for i in range(nValue):
        if i % x == 0 or i % y == 0:
            nSum += i
    # The output of the sum.
    print("The sum is: " + str(nSum))
else:
    # The output if there are errors.
    print("You've made a logic error!")
