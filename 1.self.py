class Cat:
    def __init__(self,name):
        self.name=name
    def meow(self):
         print(self.name,'says meow.')
c1=Cat('kitty')
c1.meow()