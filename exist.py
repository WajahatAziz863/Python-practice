#Check if a word exists in a sentence
sentence=input("Enter sentence:")
word=input("Enter word:")
if word.lower() in sentence.lower():
  print("yes")
else:
  print("No")