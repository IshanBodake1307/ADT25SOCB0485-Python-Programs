# len_type.py
# This program demonstrates the use of len() and type() functions
# len() returns the length (number of items) of an object
# type() returns the data type of a variable

# --- Using len() ---
print("--- len() Examples ---")

# Length of a string
text = "Hello"
print("String:", text, "-> Length:", len(text))

# Length of a list
numbers = [10, 20, 30, 40, 50]
print("List:", numbers, "-> Length:", len(numbers))

# Length of a tuple
fruits = ("apple", "banana", "mango")
print("Tuple:", fruits, "-> Length:", len(fruits))

# Length of a dictionary
student = {"name": "Amit", "age": 20, "city": "Mumbai"}
print("Dictionary:", student, "-> Length:", len(student))


# --- Using type() ---
print("\n--- type() Examples ---")

# Checking type of different variables
a = 10
b = 3.14
c = "Hello"
d = True
e = [1, 2, 3]
f = (1, 2, 3)
g = {"key": "value"}

print("Type of", a, "is", type(a))
print("Type of", b, "is", type(b))
print("Type of", c, "is", type(c))
print("Type of", d, "is", type(d))
print("Type of", e, "is", type(e))
print("Type of", f, "is", type(f))
print("Type of", g, "is", type(g))

# Example Output:
# --- len() Examples ---
# String: Hello -> Length: 5
# List: [10, 20, 30, 40, 50] -> Length: 5
# --- type() Examples ---
# Type of 10 is <class 'int'>
# Type of 3.14 is <class 'float'>
