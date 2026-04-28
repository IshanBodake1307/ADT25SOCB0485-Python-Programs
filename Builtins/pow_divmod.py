# pow_divmod.py
# This program demonstrates the use of pow() and divmod() functions
# pow(base, exp) returns base raised to the power of exp
# divmod(a, b) returns quotient and remainder as a tuple

print("--- pow() Examples ---")

# Example 1: Simple power calculation
print("pow(2, 3) =", pow(2, 3))       # 2^3 = 8
print("pow(5, 2) =", pow(5, 2))       # 5^2 = 25
print("pow(10, 0) =", pow(10, 0))     # 10^0 = 1
print("pow(3, 4) =", pow(3, 4))       # 3^4 = 81

# Example 2: pow with three arguments (modulus)
# pow(base, exp, mod) = (base^exp) % mod
print("\npow(2, 3, 5) =", pow(2, 3, 5))   # (2^3) % 5 = 8 % 5 = 3
print("pow(3, 3, 4) =", pow(3, 3, 4))     # (3^3) % 4 = 27 % 4 = 3


print("\n--- divmod() Examples ---")

# Example 1: Basic divmod
result = divmod(17, 5)
print("divmod(17, 5) =", result)       # (3, 2) -> 17/5 = 3 remainder 2
print("Quotient:", result[0])
print("Remainder:", result[1])

# Example 2: More examples
print("\ndivmod(10, 3) =", divmod(10, 3))   # (3, 1)
print("divmod(25, 4) =", divmod(25, 4))     # (6, 1)
print("divmod(100, 7) =", divmod(100, 7))   # (14, 2)

# Example 3: Practical use - Convert minutes to hours and minutes
total_minutes = 135
hours, minutes = divmod(total_minutes, 60)
print("\n" + str(total_minutes) + " minutes =", hours, "hours and", minutes, "minutes")

# Example Output:
# pow(2, 3) = 8
# divmod(17, 5) = (3, 2)
# 135 minutes = 2 hours and 15 minutes
