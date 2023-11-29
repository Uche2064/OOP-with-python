from datetime import datetime
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
    
    def updateSalary(self):
        return self.salary * Employee.raise_amount
        
    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amount = new_raise_amt
        
    @classmethod
    def from_string(cls, emps_str):
        lastName, firstName, salary = emps_str.split("-")
        return Employee(lastName, firstName, float(salary))
    
    @staticmethod
    def work_day(day):
        workday = day.weekday()
        if workday == 5 or workday == 6:
            return False
        else:
            return True 
        

emp_1 = Employee("Uche", "Lek", 150000)
emp_2 = Employee("Doe", "John", 200000)

date_xamp = datetime.date((2001,10,10))
print(Employee.work_day(date_xamp))


