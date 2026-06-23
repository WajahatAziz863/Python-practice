class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show(self):
        print('Name:',self.name)
        print('Balance:',self.balance)
class SavingsAccount(BankAccount):
    def increase(self,rate):
        interest=self.balance*rate/100
        self.balance+=interest
        print('Increased Balance:',self.balance)
s1=SavingsAccount('Wajahat Aziz',150000)
s1.show()
s1.increase(10)
s1.show()