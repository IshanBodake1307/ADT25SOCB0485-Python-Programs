# calculator_class.py
# This program demonstrates a Calculator class using OOP
# It performs basic arithmetic operations: add, subtract, multiply, divide

class Calculator:
    # Constructor to initialize two numbers
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Method to add
    def add(self):
        return self.a + self.b

    # Method to subtract
    def subtract(self):
        return self.a - self.b

    # Method to multiply
    def multiply(self):
        return self.a * self.b

    # Method to divide
    def divide(self):
        if self.b == 0:
            return "Cannot divide by zero"
        return self.a / self.b

    # Method to display all results
    def display(self):
        print("Number 1:", self.a)
        print("Number 2:", self.b)
        print("Addition:", self.add())
        print("Subtraction:", self.subtract())
        print("Multiplication:", self.multiply())
        print("Division:", self.divide())


# --- Main Program ---
if __name__ == "__main__":
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Creating object of Calculator class
    calc = Calculator(num1, num2)

    # Displaying results
    print("\n--- Calculator Results ---")
    calc.display()

    # Example Output:
    # Enter first number: 10
    # Enter second number: 3
    # --- Calculator Results ---
    # Number 1: 10.0
    # Number 2: 3.0
    # Addition: 13.0
    # Subtraction: 7.0
    # Multiplication: 30.0
    # Division: 3.3333333333333335
