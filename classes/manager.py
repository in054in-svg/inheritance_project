from classes.employee import Employee

class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)
        self.bonus = bonus  
        
    
    def title(self):
        return 'Manager'
    
    def monthly_cost(self):
        return self.salary + self.bonus