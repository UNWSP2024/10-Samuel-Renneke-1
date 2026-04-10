# Employee Class
# Samuel Renneke, 4/10/2026

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

def main():
    employee_1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    employee_2 = Employee("Mark Jones", "39119", "IT", "Programmer")
    employee_3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    employees = [employee_1, employee_2, employee_3]

    for employee in employees:
        print("Name: ", employee.name)
        print("ID number: ", employee.id_number)
        print("Department: ", employee.department)
        print("Job title: ", employee.job_title)

if __name__ == "__main__":
    main()
