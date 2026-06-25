class Bank:
    def withdraw(self,amount):
        print('Withdrawing amount:',amount)
class ATM(Bank):
    def withdraw(self,amount):
        super().withdraw(amount)
        if amount>10000:
            print('Limit exceeded.')
        else:
            print('Transaction successful.')
a1=ATM()
a1.withdraw(5000)