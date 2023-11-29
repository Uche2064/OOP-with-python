class Employee:

    raise_amount = 1.04
    nb_of_emps = 0
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.email = firstName + '.' + lastName + "@company.com"
        Employee.nb_of_emps += 1
        
    def fullname(self):
        return "{} {}".format(self.firstName,  self.lastName)
    
    def updateSalary(self, salary):
        salary =  (salary * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, salary):
        cls.salary = salary
        
print(Employee.nb_of_emps)
        
emp_1 = Employee("Uche", "Lek", 150000)

print(Employee.nb_of_emps)

