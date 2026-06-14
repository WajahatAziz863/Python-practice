class Student:
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks
    def display(self):
         print('Name:',self.name)
         print('Marks are:',self.marks)
    def add_marks(self,improve):
         self.marks=self.marks+improve
         print('Improved marks:',self.marks)
    def grade(self):
         if self.marks>=80:
              print('Grade A')
         elif self.marks>=50:
              print('Grade B')
         elif self.marks<50:
              print('Grade F')
s1=Student('Wajahat Aziz',77)
s1.display()
s1.grade()
s1.add_marks(15)
s1.display()
s1.grade()