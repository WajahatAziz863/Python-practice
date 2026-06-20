from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass 
class Creditcard(Payment):
    def pay(self,amount):
        print('Amount is:',amount)
        print('Processing Creditcard payment.')
class Debitcard(Payment):
    def pay(self,amount):
        print('Amount is:',amount)
        print('Processing Debitcard payment.')
class Mobilewallet(Payment):
    def pay(self,amount):
        print('Amount is:',amount)
        print('Processing Mobilewallet payment.')
methods=[Creditcard(),Debitcard(),Mobilewallet()]
for m in methods:
    m.pay(7000)
    print()