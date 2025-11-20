def is_palindrome(n):
    # Convert number to string and check if it reads the same forwards and backwards
    return str(n) == str(n)[::-1]

def find_largest_palindrome():
    max_palindrome = 0
    factors = (0, 0)

    # Loop through all 3-digit numbers in reverse for efficiency
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  # Start from i to avoid duplicate pairs
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                factors = (i, j)

    return max_palindrome, factors

# Run the function and print the result
palindrome, (a, b) = find_largest_palindrome()
print(f"The largest palindrome is {palindrome} = {a} × {b}")


