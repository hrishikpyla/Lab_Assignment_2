class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting option. Please choose 1, 2, or 3.")

    def print_table(self):
        print("Employee ID\tName\t\tAge\tSalary (PM)")
        for emp in self.employees:
            print(f"{emp.emp_id}\t\t{emp.name}\t\t{emp.age}\t{emp.salary}")

def main():
    emp_table = EmployeeTable()

    # Adding employees to the table
    emp_table.add_employee(Employee("161E90", "Ramu", 35, 59000))
    emp_table.add_employee(Employee("171E22", "Tejas", 30, 82100))
    emp_table.add_employee(Employee("171G55", "Abhi", 25, 100000))
    emp_table.add_employee(Employee("152K46", "Jaya", 32, 85000))

    # Getting sorting option from the user
    sort_option = int(input("Choose sorting option (1. Age, 2. Name, 3. Salary): "))

    # Sorting employees based on the chosen option
    emp_table.sort_employees(sort_option)

