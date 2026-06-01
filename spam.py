#check spam messages
s1="click this"
s2="Earn money"
s3="Subscribe now"
line=input("Enter message:")
if(s1 in line or s2 in line or s3 in line):
    print("This is spam")
else:
    print("This is not a spam")    