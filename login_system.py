class LoginSystem:
    def set_account(self,username,password):
        self.__username=username
        self.__password=password
        self.__loginattempts=0
    def login(self,username,password):
        if self.__loginattempts>=3:
            print('Account blocked.')
            return
        if self.__username==username and self.__password==password:
            print('Login successful.')
            self.__loginattempts=0
        else:
            print('Invalid credentials.')
            self.__loginattempts+=1
    def show_attempts(self):
        print('Login attempts:',self.__loginattempts)
    def is_locked(self):
        return self.__loginattempts>=3

l1=LoginSystem()
l1.set_account('Wajahat Aziz','w@jahat_123')
while True:
  username=input('Enter name:')
  password=input('Enter password:')
  l1.login(username,password)
  l1.show_attempts()
  if l1.is_locked():
   break

    

        