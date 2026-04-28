# simple_interest.py
# This program calculates Simple Interest
# Formula: SI = (P * R * T) / 100
# Where P = Principal, R = Rate of interest, T = Time in years

# Taking input from user
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

# Calculate Simple Interest
si = (p * r * t) / 100

# Calculate Total Amount
total = p + si

# Display result
print("Simple Interest =", si)
print("Total Amount =", total)

# Example Output:
# Enter Principal amount: 1000
# Enter Rate of interest: 5
# Enter Time (in years): 3
# Simple Interest = 150.0
# Total Amount = 1150.0
