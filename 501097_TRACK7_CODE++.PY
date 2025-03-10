import pandas as pd

# Define the range and output path
lower = 100000000000000
upper = 10000000000000000
output_path = "E:\\My PenDrive\\PRIME NUMBERS SUMMARY\\SPACE PROGRAMMING SERIES\\MODULE6\\501097\\501097_T7.xlsx"

# List to store prime numbers
prime_numbers = []

print("Prime numbers between", lower, "and", upper, "ending with 501097 are:")

for num in range(lower, upper + 1):
    if str(num).endswith("501097"):
        # Check if the number is prime
        if num > 1:  # all prime numbers are greater than 1
            for i in range(2, int(num ** 0.5) + 1):  # Optimize the loop up to sqrt(num)
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
                print(num)

# Create a DataFrame from the list of prime numbers
df = pd.DataFrame(prime_numbers, columns=["Prime Numbers7"])

# Save the DataFrame to an Excel file
df.to_excel(output_path, index=False)

print(f"Prime numbers saved to {output_path}")
