class ATM:
    def set_acount(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
        self.__is_verified=False
        self.__attempts=0
        if balance<0:
            self.__balance=0
    def verify_pin(self,pin):
        if self.__attempts>=3:
            print('Card is blocked.')
            return
        if self.__pin==pin:
            print('Access granted.')
            self.__is_verified=True
            self.__attempts=0
        else:
            print('Wrong PIN.')
            self.__attempts+=1
    def withdraw(self,amount):
        if not self.__is_verified:
           print('Please verify pin first.')
           return
        if amount>self.__balance:
             print('Insufficient Balance.')
        else:
            self.__balance-=amount
            print('Remaining Balance:',self.__balance)
    def check_balance(self):
        if not self.__is_verified:
            print('Please verify pin first.')
            return
        print('Balance is:',self.__balance)
    def is_blocked(self):
        return  self.__attempts>=3
    def is_verified(self):
        return self.__is_verified           
a1=ATM()
a1.set_acount(1280,20000)
while True:  
   pin=int(input('Enter pin:'))
   a1.verify_pin(pin)
   if a1.is_blocked():
       break
   if a1.is_verified():
     a1.withdraw(5000)
     a1.check_balance()
     break


