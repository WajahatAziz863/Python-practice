class Bird:
    def fly(self):
        print('Birds can fly.')
class Sparrow(Bird):
    def fly(self):
        print('Sparrows can fly.')
class Ostrich(Sparrow):
    def fly(self):
        print('Ostrich can not fly.')
o1=Bird()
o2=Sparrow()
o3=Ostrich()
o1.fly()
o2.fly()
o3.fly()