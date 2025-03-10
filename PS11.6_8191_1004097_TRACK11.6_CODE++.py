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

def generate_and_process_combinations(base_value, lower, upper, output_path, batch_size=1000):
    """Generate combinations and process them in batches to reduce memory usage."""
    x_indices = [i for i, char in enumerate(base_value) if char == 'X']

    # Ensure the input value has at least one 'X' placeholder
    if not x_indices:
        raise ValueError("The base_value must contain at least one 'X'.")

    prime_numbers = []

    for r in range(1, min(15, len(x_indices) + 1)):  # Limit 'X' replacements to 1-14
        for indices in itertools.combinations(x_indices, r):
            for digits in itertools.product(range(10), repeat=r):
                candidate = list(base_value)
                for idx, digit in zip(indices, digits):
                    candidate[idx] = str(digit)
                candidate_value = ''.join(candidate)

                # Ensure no placeholders remain and check for range and primality
                if 'X' not in candidate_value:
                    candidate_number = int(candidate_value)
                    if lower <= candidate_number <= upper and is_prime(candidate_number):
                        prime_numbers.append(candidate_number)

                # Save results in batches to reduce memory usage
                if len(prime_numbers) >= batch_size:
                    save_to_excel(prime_numbers, output_path)
                    prime_numbers.clear()  # Clear the list after saving

    # Save any remaining primes
    if prime_numbers:
        save_to_excel(prime_numbers, output_path)

def save_to_excel(numbers, output_path):
    """Save a list of numbers to an Excel file."""
    df = pd.DataFrame(numbers, columns=["Prime Numbers"])
    try:
        with pd.ExcelWriter(output_path, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, index=False, header=not writer.sheets)
    except FileNotFoundError:
        # Save normally if the file does not exist
        df.to_excel(output_path, index=False)

# Define the range and output path
lower = 25000
upper = 10**19  # Restrict range to 19-digit numbers
output_path = "E:\\My PenDrive\\PRIME NUMBERS SUMMARY\\SPACE PROGRAMMING SERIES\\MODULE16\\1004097\\PS11.6_8191_1004097.xlsx"

# Input 19-digit number with 'X' as placeholder for any digit (must have 1-14 'X's)
base_value = 'XXX8191XXXXX1004097'

try:
    # Generate combinations and process them in a memory-efficient way
    generate_and_process_combinations(base_value, lower, upper, output_path)

    print(f"Prime numbers saved to {output_path}")

except ValueError as e:
    print(f"Error: {e}")
except MemoryError as e:
    print("MemoryError: The program ran out of memory. Consider reducing the size of the input.")
