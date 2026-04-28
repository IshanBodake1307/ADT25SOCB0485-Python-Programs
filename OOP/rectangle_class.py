# rectangle_class.py
# This program demonstrates a Rectangle class using OOP
# It calculates area and perimeter of a rectangle

class Rectangle:
    # Constructor to initialize length and breadth
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Method to calculate area
    def area(self):
        return self.length * self.breadth

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    # Method to display details
    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


# --- Main Program ---
if __name__ == "__main__":
    # Taking input from user
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))

    # Creating object of Rectangle class
    rect = Rectangle(l, b)

    # Displaying result
    print("\n--- Rectangle Details ---")
    rect.display()

    # Example Output:
    # Enter length: 5
    # Enter breadth: 3
    # --- Rectangle Details ---
    # Length: 5.0
    # Breadth: 3.0
    # Area: 15.0
    # Perimeter: 16.0
