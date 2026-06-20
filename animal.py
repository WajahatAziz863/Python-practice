from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
     print('Dog barks')
class Cat(Animal):
   def sound(self):
      print('cat meows.')
d1=Dog()
d1.sound()
c1=Cat()
c1.sound()