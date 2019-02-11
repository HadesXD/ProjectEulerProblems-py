# 
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 10
b = 10
c = 1 
big = 1

def Reverse(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r

while a < 100:
    while b < 100:
        c = a * b
        if c > big:
            print(Reverse(c))
        b += 1
    b = 100
    a += 1
