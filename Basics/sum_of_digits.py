# sum_of_digits.py
# This program finds the sum of digits of a number
# Example: 1234 -> 1 + 2 + 3 + 4 = 10

# Taking input from user
num = int(input("Enter a number: "))

# Store original number
temp = num
sum = 0

# Extract digits one by one and add them
while temp > 0:
    digit = temp % 10    # Get last digit
    sum = sum + digit    # Add digit to sum
    temp = temp // 10    # Remove last digit

# Display result
print("Sum of digits of", num, "is", sum)

# Example Output:
# Enter a number: 1234
# Sum of digits of 1234 is 10
