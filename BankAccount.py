class BankAccount:
    def __init__(self,name,balance):
        self.__name=name
        if balance<0:
            print('Invalid Balance.Setting to 0')
            self.__balance=0
        else:
            self.__balance=balance
    def deposit(self,amount):
        print('Deposit amount:',amount)
        if amount<=0:
            print('Invalid Deposit amount.')
        else:
            self.__balance+=amount
        print('Balance after deposit:',self.__balance)
    def withdraw(self,amount):
        print('Withdraw amount:',amount)
        if amount>self.__balance:
            print('Insufficient Balance.')
        else:
            self.__balance-=amount
        print('Balance after withdraw:',self.__balance)
    def show(self):
        print('Name:',self.__name)
        print('Balance:',self.__balance)
name=input('Enter name:')
balance=int(input('Enter balance:'))
s1=BankAccount(name,balance)
s1.deposit(5000)
s1.withdraw(4000)
s1.show()
        
    