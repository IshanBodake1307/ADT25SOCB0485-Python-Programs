# any_all.py
# This program demonstrates the use of any() and all() functions
# any() returns True if ANY item in the list is True
# all() returns True if ALL items in the list are True

print("--- any() Examples ---")

# Example 1: Check if any value is True
list1 = [False, False, True, False]
print("List:", list1)
print("any() result:", any(list1))   # True (because one True exists)

# Example 2: Check if any number is positive
numbers = [-1, -2, -3, 5, -4]
result = any(n > 0 for n in numbers)
print("\nNumbers:", numbers)
print("Any positive?", result)   # True

# Example 3: All False values
list2 = [False, False, False]
print("\nList:", list2)
print("any() result:", any(list2))   # False

# Example 4: Empty list
print("\nEmpty list:", any([]))   # False


print("\n--- all() Examples ---")

# Example 1: Check if all values are True
list3 = [True, True, True]
print("List:", list3)
print("all() result:", all(list3))   # True

# Example 2: Check if all numbers are positive
numbers2 = [1, 2, 3, 4, 5]
result2 = all(n > 0 for n in numbers2)
print("\nNumbers:", numbers2)
print("All positive?", result2)   # True

# Example 3: One False value
list4 = [True, True, False, True]
print("\nList:", list4)
print("all() result:", all(list4))   # False

# Example 4: Check if all marks are passing (above 40)
marks = [55, 60, 45, 70, 80]
all_passed = all(m >= 40 for m in marks)
print("\nMarks:", marks)
print("All passed?", all_passed)   # True

# Example Output:
# List: [False, False, True, False]
# any() result: True
# All positive? True
