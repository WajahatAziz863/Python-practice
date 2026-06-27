class BankAccount:
    def transaction(self,amount):
        print('Processing transaction of:',amount)
class SavingsAccount(BankAccount):
    def transaction(self,amount):
        super().transaction(amount)
        if amount>10000:
            print('Withdrawal limit exceeded for savingsaccount.')
        else:
            print('Savings transaction successful.')
class CurrentAccount(BankAccount):
    def transaction(self,amount):
        super().transaction(amount)
        if amount>50000:
            print('Large transaction flagged for review.')
        else:
            print('Current account transaction successful.')
class StudentAccount(BankAccount):
    def transaction(self,amount):
        super().transaction(amount)
        if amount>5000:
            print('Student account limit exceeded.')
        else:
            print('Student transaction successful.')
b1=BankAccount()
s1=SavingsAccount()
c1=CurrentAccount()
s2=StudentAccount()
data=[b1,s1,c1,s2]
for a in data:
    a.transaction(5000)