# interest_class.py
# This program demonstrates an Interest class using OOP
# It calculates Simple Interest and Compound Interest

class Interest:
    # Constructor to initialize principal, rate, and time
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    # Method to calculate Simple Interest
    # Formula: SI = (P * R * T) / 100
    def simple_interest(self):
        si = (self.principal * self.rate * self.time) / 100
        return si

    # Method to calculate Compound Interest
    # Formula: CI = P * (1 + R/100)^T - P
    def compound_interest(self):
        amount = self.principal * ((1 + self.rate / 100) ** self.time)
        ci = amount - self.principal
        return ci

    # Method to display results
    def display(self):
        print("Principal:", self.principal)
        print("Rate:", self.rate, "%")
        print("Time:", self.time, "years")
        print("Simple Interest:", self.simple_interest())
        print("Compound Interest:", round(self.compound_interest(), 2))


# --- Main Program ---
if __name__ == "__main__":
    # Taking input from user
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))

    # Creating object of Interest class
    obj = Interest(p, r, t)

    # Displaying results
    print("\n--- Interest Calculation ---")
    obj.display()

    # Example Output:
    # Enter principal amount: 10000
    # Enter rate of interest: 5
    # Enter time in years: 3
    # --- Interest Calculation ---
    # Principal: 10000.0
    # Rate: 5.0 %
    # Time: 3.0 years
    # Simple Interest: 1500.0
    # Compound Interest: 1576.25
