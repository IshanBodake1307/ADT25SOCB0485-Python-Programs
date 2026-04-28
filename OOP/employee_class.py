# employee_class.py
# This program demonstrates an Employee class using OOP
# It stores employee details and calculates salary

class Employee:
    # Constructor to initialize employee details
    def __init__(self, name, emp_id, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary

    # Method to calculate gross salary
    def gross_salary(self):
        hra = self.basic_salary * 0.20   # 20% of basic
        da = self.basic_salary * 0.50    # 50% of basic
        gross = self.basic_salary + hra + da
        return gross

    # Method to display employee details
    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Basic Salary:", self.basic_salary)
        print("Gross Salary:", self.gross_salary())


# --- Main Program ---
if __name__ == "__main__":
    # Taking input from user
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    salary = float(input("Enter basic salary: "))

    # Creating object of Employee class
    emp = Employee(name, emp_id, salary)

    # Displaying result
    print("\n--- Employee Details ---")
    emp.display()

    # Example Output:
    # Enter employee name: Rahul
    # Enter employee ID: E101
    # Enter basic salary: 30000
    # --- Employee Details ---
    # Name: Rahul
    # Employee ID: E101
    # Basic Salary: 30000.0
    # Gross Salary: 51000.0
