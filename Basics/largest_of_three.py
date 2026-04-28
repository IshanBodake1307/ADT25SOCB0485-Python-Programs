# largest_of_three.py
# This program finds the largest of three numbers
# It uses simple if-elif-else conditions

# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Compare using if-elif-else
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Display result
print("The largest number is", largest)

# Example Output:
# Enter first number: 10
# Enter second number: 25
# Enter third number: 15
# The largest number is 25.0
