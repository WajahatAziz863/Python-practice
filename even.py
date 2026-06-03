#printing even numbers from 0 to 20
for number in range(0,21):
 if number%2==0:
  print(number)
#Another simple way
for number in range(0,21,2):#range(start,stop,step)
 print(number)