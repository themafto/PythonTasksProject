class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls, strr):
        name, salary = strr.split(', ')
        return cls(name, float(salary))

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def is_high_salary(self, salary):
        if self.salary > 100000:
            return "Is salary high? -> ", True
        else:
            return "Salary is low"

employ_str = "VAsilisa, 150000"
employee = Employee.from_string(employ_str)
print(employee)
print(employee.is_high_salary(150000))




