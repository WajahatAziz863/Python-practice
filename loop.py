#Looping through a dictionary
line={
    'Aslam':'red',
    'zonto':'yellow',
    'fonsi':'green',
    'year':1973
}
for a in line:
    print(a) #this will print only keys
#If we want to print all the values
for b,c in line.items():
    print(b,c)    