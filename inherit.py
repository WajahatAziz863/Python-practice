class Person:
    def show_name(self):
        print('I am a person.')
class Student(Person):
    def study(self):
        print('student is studying.')
s1=Student()
s1.show_name()
s1.study()
#Next question
class Vehicle:
    def start(self):
        print('Vehicle is starting.')
class Car(Vehicle):
    def drive(self):
        print('Car is driving.')
c1=Car()
c1.start()
c1.drive()