import Employee
class Developer(Employee):
    def __init__(self, firstname, lastname, salary, prog_lang):
        super().__init__(self, firstname, lastname, salary)
        self.prog_lang = prog_lang