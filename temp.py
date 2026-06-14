class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def show(self):
        print('Original Temperature is:',self.celsius)
    def increase(self,inc):
        self.celsius+=inc
        print('Increased Temp:',self.celsius)
    def decrease(self,dec):
        self.celsius-=dec
        print('Decreased Temp:',self.celsius)
    def check(self):
        if self.celsius>=30:
            print('Hot')
        elif self.celsius>=15 and self.celsius<30:
            print('Normal')
        elif self.celsius<15:
            print('Cold')
t1=Temperature(12)
t1.show()
t1.check()
t1.increase(20)
t1.show()
t1.check()
t1.decrease(10)
t1.show()
t1.check()