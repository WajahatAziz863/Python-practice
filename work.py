class Employee:
    def work(self):
        print('Employee is working.')
class Developer(Employee):
    def work(self):
        print('Developer is writing code.')
class Designer(Employee):
    def work(self):
        print('Designer is designing UI.')
class Manager(Employee):
    def work(self):
        print('Manager is managing team.')
e1=Employee()
d1=Developer()
d2=Designer()
m1=Manager()
data=[Employee(),Developer(),Designer(),Manager()]#you can also write it as,data=[e1,d1,d2,m1],this is also correct.
for a in data:#data here is just variable storing values
    a.work()