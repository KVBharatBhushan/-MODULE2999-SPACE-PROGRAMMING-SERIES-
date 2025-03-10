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

    # Ensure the input value has at least one 'X' placeholder
    if not x_indices:
        raise ValueError("The base_value must contain at least one 'X'.")

    for r in range(1, min(15, len(x_indices) + 1)):  # Limit 'X' replacements to 1-14
        for indices in itertools.combinations(x_indices, r):
            for digits in itertools.product(range(10), repeat=r):
                candidate = list(base_value)
                for idx, digit in zip(indices, digits):
                    candidate[idx] = str(digit)
                candidate_value = ''.join(candidate)
                if 'X' not in candidate_value:  # Ensure no placeholders remain
                    combinations.append(int(candidate_value))

    return combinations

# Define the range and output path
lower = 25000
upper = 10**19  # Restrict range to 19-digit numbers
output_path = "E:\\My PenDrive\\PRIME NUMBERS SUMMARY\\SPACE PROGRAMMING SERIES\\MODULE16\\1004097\\PS11.1_ALFA8_1004097.xlsx"

# Input 19-digit number with 'X' as placeholder for any digit (must have 1-14 'X's)
base_value = 'XX21474836471004097'

try:
    # Generate combinations and check for prime numbers within the specified range
    combinations = generate_combinations(base_value)
    prime_combinations = [num for num in combinations if is_prime(num) and lower <= num <= upper]

    # Save the prime numbers to an Excel file
    df = pd.DataFrame(prime_combinations, columns=["Prime Numbers"])
    df.to_excel(output_path, index=False)

    print(f"Prime numbers saved to {output_path}")

except ValueError as e:
    print(f"Error: {e}")
