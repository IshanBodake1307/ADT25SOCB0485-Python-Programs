# conversions.py
# This program demonstrates type conversion functions in Python
# int(), float(), str(), list(), tuple(), set()

print("--- Type Conversion Examples ---")

# --- int() : Convert to integer ---
print("\n1. int() - Convert to integer")
a = int(3.7)       # float to int
b = int("25")      # string to int
print("int(3.7) =", a)
print('int("25") =', b)

# --- float() : Convert to float ---
print("\n2. float() - Convert to float")
c = float(10)       # int to float
d = float("3.14")   # string to float
print("float(10) =", c)
print('float("3.14") =', d)

# --- str() : Convert to string ---
print("\n3. str() - Convert to string")
e = str(100)        # int to string
f = str(3.14)       # float to string
print("str(100) =", e, "Type:", type(e))
print("str(3.14) =", f, "Type:", type(f))

# --- list() : Convert to list ---
print("\n4. list() - Convert to list")
g = list("hello")           # string to list
h = list((1, 2, 3, 4))      # tuple to list
print('list("hello") =', g)
print("list((1,2,3,4)) =", h)

# --- tuple() : Convert to tuple ---
print("\n5. tuple() - Convert to tuple")
i = tuple([10, 20, 30])     # list to tuple
print("tuple([10,20,30]) =", i)

# --- set() : Convert to set (removes duplicates) ---
print("\n6. set() - Convert to set")
j = set([1, 2, 2, 3, 3, 4])
print("set([1,2,2,3,3,4]) =", j)

# Example Output:
# int(3.7) = 3
# float(10) = 10.0
# list("hello") = ['h', 'e', 'l', 'l', 'o']
