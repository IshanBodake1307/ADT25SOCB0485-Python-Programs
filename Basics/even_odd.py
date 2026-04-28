# even_odd.py
# This program checks if a number is even or odd
# Even numbers are divisible by 2 (remainder = 0)
# Odd numbers are not divisible by 2 (remainder = 1)

# Taking input from user
num = int(input("Enter a number: "))

# Check using modulus operator
if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")

# Example Output:
# Enter a number: 7
# 7 is an Odd number
