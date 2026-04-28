# prime_number.py
# This program checks whether a number is prime or not
# A prime number is greater than 1 and divisible only by 1 and itself
# Example: 2, 3, 5, 7, 11 are prime numbers

# Taking input from user
num = int(input("Enter a number: "))

# Flag to check if prime
is_prime = True

# Numbers less than or equal to 1 are not prime
if num <= 1:
    is_prime = False
else:
    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Display result
if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

# Example Output:
# Enter a number: 7
# 7 is a Prime number
