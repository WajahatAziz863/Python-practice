class Shape:
    def area(self):
        print('Calculating area.')
class Circle(Shape):
    def area(self):
        print('Area of circle.')
c1=Circle()
c1.area() #This code is replacing parent class message with child class through method overriding.

#Now we will print both parent and child class messages.
class Shape:
    def area(self):
        print('Calculating area.')
class Circle(Shape):
    def area(self):
        super().area()
        print('Area of circle.')
c1=Circle()
c1.area()