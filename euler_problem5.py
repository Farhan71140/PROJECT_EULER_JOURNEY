# Question:
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# (i.e., find the Least Common Multiple (LCM) of numbers 1 through 20)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Compute LCM of numbers from 1 to 20
result = 1
for num in range(1, 21):
    result = lcm(result, num)

print("Smallest number divisible by 1 to 20 is:", result)