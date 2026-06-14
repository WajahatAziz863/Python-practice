class Mobile:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def model(self,name):
        self.name=name
    def balance(self,price):
        self.price=price
    def show(self):
        print('Mobile Model:',self.name)
        print('Price:',self.price)
m1=Mobile('Samsung',85000)
m1.model('Samsung')
m1.balance(85000)
m1.show()