# max_min_sum.py
# This program demonstrates the use of max(), min(), and sum() functions
# max() returns the largest value
# min() returns the smallest value
# sum() returns the total of all values

print("--- max(), min(), sum() Examples ---")

# Using with a list
numbers = [10, 25, 5, 40, 15]
print("List:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Using with a tuple
marks = (85, 92, 78, 90, 88)
print("\nTuple:", marks)
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Total marks:", sum(marks))

# Using max and min with individual values
print("\nmax(10, 20, 30) =", max(10, 20, 30))
print("min(10, 20, 30) =", min(10, 20, 30))

# Using max and min with strings (alphabetical order)
print("\nmax('apple', 'banana', 'cherry') =", max("apple", "banana", "cherry"))
print("min('apple', 'banana', 'cherry') =", min("apple", "banana", "cherry"))

# Example Output:
# List: [10, 25, 5, 40, 15]
# Maximum: 40
# Minimum: 5
# Sum: 95
