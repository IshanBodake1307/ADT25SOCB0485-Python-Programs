# palindrome.py
# This program checks if a string or number is a palindrome
# A palindrome reads the same forwards and backwards
# Example: "madam", "121" are palindromes

# Taking input from user
text = input("Enter a string or number: ")

# Reverse the string
reverse = text[::-1]

# Compare original and reversed
if text == reverse:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")

# Example Output:
# Enter a string or number: madam
# madam is a Palindrome
