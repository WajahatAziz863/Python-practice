class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print('Name:',self.name)
        print('Balance:',self.balance)
a1=Account('Wazir',35000)
a1.display()