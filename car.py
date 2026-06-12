class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def fun(self):
        print(self.name,' is moving.')
        print('Color is ',self.color)
c1=Car('Fortuner','Red')
c1.fun()  