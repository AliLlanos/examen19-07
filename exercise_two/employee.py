class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def change_salary(self, new_salary):
        self.salary = new_salary


if __name__ == "__main__":

    employee = Employee("Juan Martines", 24000)
    print(f"{employee.name}:€{employee.get_salary()}")

    update_salary = 30000
    employee.change_salary(update_salary)
    print(f"{employee.name}: €{employee.get_salary()}")
