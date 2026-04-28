# fibonacci.py
# This program prints the Fibonacci series up to N terms
# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the sum of the two numbers before it

# Taking input from user
n = int(input("Enter number of terms: "))

# First two terms
a = 0
b = 1

print("Fibonacci series:")

# Loop to print Fibonacci series
for i in range(n):
    print(a, end=" ")
    # Calculate next term
    temp = a + b
    a = b
    b = temp

print()  # new line at end

# Example Output:
# Enter number of terms: 8
# Fibonacci series:
# 0 1 1 2 3 5 8 13
