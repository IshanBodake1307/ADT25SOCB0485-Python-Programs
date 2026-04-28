# factorial_function.py
# This program finds the factorial of a number using a function
# Factorial of n = 1 * 2 * 3 * ... * n

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# --- Main Program ---
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers")
    else:
        result = factorial(num)
        print("Factorial of", num, "is", result)

    # Example Output:
    # Enter a number: 5
    # Factorial of 5 is 120
