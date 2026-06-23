class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
       print('Name:',self.name)
       print('Age:',self.age)
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def display_marks(self):
        print('Marks:',self.marks)

name=input('Enter name:')
age=int(input('Enter Age:'))
marks=int(input('Enter marks:'))
s1=Student(name,age,marks)
s1.display()
s1.display_marks()        
