# student_class.py
# This program demonstrates a Student class using OOP
# It stores student details and calculates percentage and grade

class Student:
    # Constructor to initialize student details
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks   # marks is a list of subject marks

    # Method to calculate total marks
    def total(self):
        total = 0
        for m in self.marks:
            total = total + m
        return total

    # Method to calculate percentage
    def percentage(self):
        per = self.total() / len(self.marks)
        return per

    # Method to find grade
    def grade(self):
        per = self.percentage()
        if per >= 90:
            return "A+"
        elif per >= 80:
            return "A"
        elif per >= 70:
            return "B"
        elif per >= 60:
            return "C"
        elif per >= 40:
            return "D"
        else:
            return "Fail"

    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())


# --- Main Program ---
if __name__ == "__main__":
    # Taking input from user
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    n = int(input("Enter number of subjects: "))
    marks = []
    for i in range(n):
        m = float(input("Enter marks for subject " + str(i + 1) + ": "))
        marks.append(m)

    # Creating object of Student class
    s = Student(name, roll, marks)

    # Displaying result
    print("\n--- Student Report Card ---")
    s.display()

    # Example Output:
    # Enter student name: Amit
    # Enter roll number: 101
    # Enter number of subjects: 3
    # Enter marks for subject 1: 85
    # Enter marks for subject 2: 90
    # Enter marks for subject 3: 78
    # --- Student Report Card ---
    # Name: Amit
    # Roll No: 101
    # Marks: [85.0, 90.0, 78.0]
    # Total: 253.0
    # Percentage: 84.33 %
    # Grade: A
