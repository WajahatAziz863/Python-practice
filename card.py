class Payment:
    def pay(self,amount):
        print('Processing payment of:',amount)
class CreditCard(Payment):
    def pay(self,amount):
        super().pay(amount)
        print('Paid using credit card.')
class DebitCard(Payment):
    def pay(self,amount):
        super().pay(amount)
        print('Paid using Debit card.')
class JazzCash(Payment):
    def pay(self,amount):
        super().pay(amount)
        print('Paid using Mobile wallet.')
p1=Payment()
c1=CreditCard()
d1=DebitCard()
j1=JazzCash()
data=[p1,c1,d1,j1]
for a in data:
    a.pay(5000)