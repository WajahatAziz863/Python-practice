class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print('Name:',self.name)
        print('Age:',self.age)
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display_employee(self):
        print('Salary is:',self.salary)
class Manager(Employee):
    def __init__(self,name,age,salary,bonus):
        super().__init__( name,age,salary)
        self.bonus=bonus
    def total_income(self):
        total=self.salary+self.bonus
        print('Salary after bonus:',total)
name=input('Enter name:')
age=int(input('Enter age:'))
salary=int(input('Enter salary:'))
bonus=int(input('Enter bonus:'))
m1=Manager(name,age,salary,bonus)
m1.display_person()
m1.display_employee()
m1.total_income()