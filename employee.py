class Employee:
    def __init__(self,name,salary):
         self.name=name
         self.salary=salary
    def display(self):
        print('Name:',self.name)
        print('Salary:',self.salary)
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def total_salary(self):
        total=self.salary+self.bonus
        print('Total Salary:',total)
name=input('Enter name:')
salary=int(input('Enter salary:'))
bonus=int(input('Enter bonus:'))
m1=Manager(name,salary,bonus)
m1.display()
m1.total_salary()
               