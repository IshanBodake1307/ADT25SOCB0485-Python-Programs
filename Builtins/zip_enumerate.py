# zip_enumerate.py
# This program demonstrates the use of zip() and enumerate() functions
# zip() combines two or more lists element-wise
# enumerate() adds index numbers to items in a list

print("--- zip() Examples ---")

# Example 1: Combine two lists
names = ["Amit", "Priya", "Rahul"]
marks = [85, 92, 78]

# Using zip to pair names with marks
combined = list(zip(names, marks))
print("Names:", names)
print("Marks:", marks)
print("Combined:", combined)

# Looping through zipped lists
print("\nStudent Results:")
for name, mark in zip(names, marks):
    print(name, "->", mark)

# Example 2: Zip three lists
subjects = ["Math", "Science", "English"]
print("\nSubject-wise results:")
for name, sub, mark in zip(names, subjects, marks):
    print(name, "-", sub, ":", mark)


print("\n--- enumerate() Examples ---")

# Example 1: Add index to list items
fruits = ["apple", "banana", "mango", "orange"]

print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(index, "->", fruit)

# Example 2: Start index from 1
print("\nFruits with index starting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(index, "->", fruit)

# Example Output:
# Names: ['Amit', 'Priya', 'Rahul']
# Marks: [85, 92, 78]
# Combined: [('Amit', 85), ('Priya', 92), ('Rahul', 78)]
