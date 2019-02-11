# 
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

nValue = int(input("Vnesi value: "))
i = 3
m = 0

if nValue % 2 == 0:
    print(2)
    m = 2
    nValue /= 2
    print("Value is now: " + str(nValue))

while nValue >= i:
    if nValue % i == 0:
        print(i)
        nValue /= i
        if i > m:
            m = i
    i += 1

print(m)
        
