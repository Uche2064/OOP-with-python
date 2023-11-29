import Employee
class Manager(Employee):
    def __inti__(self, firstname, lastname, salary, employees=[]):
        super().__init__(firstname, lastname, salary)
        if employees != None:
            self.employees = employees
        else: 
            self.employees = []
    
    def add_emp(self, employe):
        if employe in self.employees:
            print("Employee already exist")
        else:
            self.employees.append(employe)
    
    def remove_emp(self, employe):
        if employe not in self.employees:
            print("Employee does not exist")
        else:
            self.employees.remove(employe)
            
    def print_emps(self):
        for employe in self.employees:
            print(employe.emal)