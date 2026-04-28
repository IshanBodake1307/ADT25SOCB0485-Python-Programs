# prime_function.py
# This program checks if a number is prime using a function
# A prime number is only divisible by 1 and itself

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# --- Main Program ---
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(num, "is a Prime number")
    else:
        print(num, "is not a Prime number")

    # Example Output:
    # Enter a number: 7
    # 7 is a Prime number
