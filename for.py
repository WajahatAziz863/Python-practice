#counting vowels in a word through for loop
enter=input("Enter your name:")
count=0
for word in enter.lower():
 if word in "aeiou":
  count=count+1

print("vowels are:",count)   
      