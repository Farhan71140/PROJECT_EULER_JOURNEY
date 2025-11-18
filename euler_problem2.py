"""
Project Euler Problem:
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

# Python solution
a, b = 1, 2
total = 0

while b <= 4000000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b

print("Sum of even Fibonacci numbers below 4 million:", total)