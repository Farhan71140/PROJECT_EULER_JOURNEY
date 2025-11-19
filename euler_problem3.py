# Step 1: Start with the number we want to factor
number = 600851475143

# Step 2: Start checking from the smallest prime number
factor = 2

# Step 3: Loop until number becomes 1
while number > 1:
    # If 'factor' divides 'number' completely
    if number % factor == 0:
        # Divide 'number' by 'factor'
        number = number // factor
    else:
        # Move to the next possible factor
        factor += 1

# Step 4: Print the last factor used
print("Largest prime factor is:", factor)