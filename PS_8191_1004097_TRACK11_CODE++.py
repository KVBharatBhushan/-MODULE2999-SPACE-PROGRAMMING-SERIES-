import itertools
import pandas as pd

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_combinations(base_value):
    """Generate all possible combinations by replacing 'X' with digits 0-9."""
    x_indices = [i for i, char in enumerate(base_value) if char == 'X']
    combinations = []

    for r in range(1, 15):  # Vary the number of X's from 1 to 14
        for indices in itertools.combinations(range(len(base_value)), r):
            candidate = list(base_value)
            if all(candidate[idx] == 'X' for idx in indices):
                for digits in itertools.product(range(10), repeat=r):
                    for idx, digit in zip(indices, digits):
                        candidate[idx] = str(digit)
                    combinations.append(int(''.join(candidate)))

    return combinations

# Define the range and output path
lower = 25000
upper = 10000000000000000000
output_path = "E:\\My PenDrive\\PRIME NUMBERS SUMMARY\\SPACE PROGRAMMING SERIES\\MODULE16\\1004097\\PS11.1_8191_1004097.xlsx"

# Input 19-digit number with 'X' as placeholder for any digit (must have 1-14 'X's)
base_value = 'XXXXXXXX81911004097'

# Generate combinations and check for prime numbers within the specified range
combinations = generate_combinations(base_value)
prime_combinations = [num for num in combinations if is_prime(num) and lower <= num <= upper]

# Save the prime numbers to an Excel file
df = pd.DataFrame(prime_combinations, columns=["Prime Numbers"])
df.to_excel(output_path, index=False)

print(f"Prime numbers saved to {output_path}")
