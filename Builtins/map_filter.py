# map_filter.py
# This program demonstrates the use of map() and filter() functions
# map() applies a function to every item in a list
# filter() filters items based on a condition

print("--- map() Examples ---")

# Example 1: Square each number using map
numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(n):
    return n * n

# Apply map
result = list(map(square, numbers))
print("Original list:", numbers)
print("Squared list:", result)

# Example 2: Convert list of strings to integers
str_numbers = ["10", "20", "30", "40"]
int_numbers = list(map(int, str_numbers))
print("\nString list:", str_numbers)
print("Integer list:", int_numbers)


print("\n--- filter() Examples ---")

# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a function to check even
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Apply filter
even_numbers = list(filter(is_even, numbers))
print("Original list:", numbers)
print("Even numbers:", even_numbers)

# Example 2: Filter numbers greater than 5
def greater_than_5(n):
    return n > 5

result = list(filter(greater_than_5, numbers))
print("Numbers greater than 5:", result)

# Example Output:
# Original list: [1, 2, 3, 4, 5]
# Squared list: [1, 4, 9, 16, 25]
# Even numbers: [2, 4, 6, 8, 10]
