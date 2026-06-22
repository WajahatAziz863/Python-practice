class Student:
    def __init__(self):
            self.__marks=0
    def set_marks(self,marks):
          if marks<0 or marks>100:
                print('Invalid marks.')
          else:
                self.__marks=marks
    def get_marks(self):
          print('Marks:',self.__marks)
s1=Student()
s1.set_marks(95)
s1.get_marks()