# palindrome_function.py
# This program checks if a string is a palindrome using a function
# A palindrome reads the same forwards and backwards
# Example: "madam" is a palindrome

# Function to check palindrome
def is_palindrome(text):
    # Reverse the string
    reverse = text[::-1]
    if text == reverse:
        return True
    else:
        return False


# --- Main Program ---
if __name__ == "__main__":
    word = input("Enter a string: ")

    if is_palindrome(word):
        print(word, "is a Palindrome")
    else:
        print(word, "is not a Palindrome")

    # Example Output:
    # Enter a string: madam
    # madam is a Palindrome
