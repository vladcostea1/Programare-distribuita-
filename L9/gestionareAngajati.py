class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Angajat: {self.name}, Salariu: {self.salary} lei"
class Manager(Employee):
    def __init__(self, name, salary, department):
        # apel constructor clasa de bază
        super().__init__(name, salary)
        self.department = department

    # suprascriere metodă
    def get_details(self):
        return f"Manager: {self.name}, Salariu: {self.salary} lei, Departament: {self.department}"

if __name__ == "__main__":
    employee = Employee("Ion Popescu", 4000)
    manager = Manager("Ana Ionescu", 7000, "IT")

    print(employee.get_details())
    print(manager.get_details())
