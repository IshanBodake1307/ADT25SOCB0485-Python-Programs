# multiplication_table.py
# This program prints the multiplication table of a given number
# Example: Table of 5 -> 5x1=5, 5x2=10, ..., 5x10=50

# Taking input from user
num = int(input("Enter a number: "))

# Print multiplication table using for loop
print("Multiplication Table of", num)
for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

# Example Output:
# Enter a number: 5
# Multiplication Table of 5
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
