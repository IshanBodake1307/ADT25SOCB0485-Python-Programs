# fibonacci_function.py
# This program prints the Fibonacci series using a function
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each number is the sum of the two numbers before it

# Function to print Fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
    print()  # new line at end


# --- Main Program ---
if __name__ == "__main__":
    num = int(input("Enter number of terms: "))

    if num <= 0:
        print("Please enter a positive number")
    else:
        fibonacci(num)

    # Example Output:
    # Enter number of terms: 8
    # Fibonacci series:
    # 0 1 1 2 3 5 8 13
