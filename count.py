#How to count words in a sentence (words not characters)
jumla=input("Enter sentence:")
word=jumla.split()
print("No words are:",len(word))
#Another simple way
jumla=input("Enter sentence:")
print("No words are:",len(jumla.split()))
