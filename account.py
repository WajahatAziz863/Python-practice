class Account:
    def __init__(self,balance):
        self.balance=balance
        print('Original balance:',self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient Balance.')
        else:
            print('Withdrawn:',amount)
            self.balance=self.balance-amount
            print('Remaining Balance:',self.balance)
class SavingsAccount(Account):
    def withdraw(self,amount):
        super().withdraw(amount)
        if self.balance<5000:
            print('warning:Balance is low.')
s1=SavingsAccount(20000)
s1.withdraw(5000)
s1.withdraw(13000)
