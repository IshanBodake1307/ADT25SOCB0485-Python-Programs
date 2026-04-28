# armstrong.py
# This program checks if a number is an Armstrong number
# An Armstrong number: sum of each digit raised to power of number of digits = the number itself
# Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# Taking input from user
num = int(input("Enter a number: "))

# Store original number
temp = num

# Count number of digits
digits = len(str(num))

# Calculate sum of digits raised to power
sum = 0
while temp > 0:
    digit = temp % 10         # Get last digit
    sum = sum + (digit ** digits)  # Add digit^n to sum
    temp = temp // 10          # Remove last digit

# Check if Armstrong or not
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Example Output:
# Enter a number: 153
# 153 is an Armstrong number
