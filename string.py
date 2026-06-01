#6 check if word starts with capital letter
value=input("Enter a name:")
if value[0]==value[0].upper():
 print (True)
else:
 print (False)
 #Another easy method
 value=input("Enter a name:")
 print(value[0].isupper())
