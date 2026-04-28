# print_input.py
# This program demonstrates the use of print() and input() functions
# print() is used to display output
# input() is used to take input from the user

# --- Using print() ---
print("--- print() Examples ---")

# Simple print
print("Hello, World!")

# Printing multiple values
name = "Python"
version = 3
print("Language:", name, "Version:", version)

# Using end parameter (to print on same line)
print("Hello", end=" ")
print("World")

# Using sep parameter (to change separator)
print("A", "B", "C", sep="-")

# Printing numbers
print("Sum of 5 + 3 =", 5 + 3)


# --- Using input() ---
print("\n--- input() Examples ---")

# Taking string input
name = input("Enter your name: ")
print("Hello,", name)

# Taking integer input
age = int(input("Enter your age: "))
print("Your age is:", age)

# Taking float input
marks = float(input("Enter your marks: "))
print("Your marks:", marks)

# Example Output:
# --- print() Examples ---
# Hello, World!
# Language: Python Version: 3
# Hello World
# A-B-C
# Sum of 5 + 3 = 8
# --- input() Examples ---
# Enter your name: Rahul
# Hello, Rahul
