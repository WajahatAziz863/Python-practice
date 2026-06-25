class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate_bonus(self):
        self.base_bonus=self.salary*10/100
        print('Base bonus is:',self.base_bonus)
class Manager(Employee):
    def calculate_bonus(self):
        super().calculate_bonus()
        total_bonus=5000+self.base_bonus
        print('Total Bonus:',total_bonus)
name=input('Enter name:')
salary=int(input('Enter salary:'))
m1=Manager(name,salary)
m1.calculate_bonus()