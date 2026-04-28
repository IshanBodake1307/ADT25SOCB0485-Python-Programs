# factorial.py
# This program finds the factorial of a number
# Factorial of n = 1 * 2 * 3 * ... * n
# Example: Factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

# Taking input from user
num = int(input("Enter a number: "))

# Initialize factorial as 1
fact = 1

# Check for negative number
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    # Calculate factorial using for loop
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)

# Example Output:
# Enter a number: 5
# Factorial of 5 is 120
