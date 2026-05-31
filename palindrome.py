#Check if a word is palindrome(mean whether the word is same if we read it at the start or at the end ) or not
word=input("Enter a word:").lower()
name=word[::-1]
if word==name:
 print("Yes")
else:
 print("No")
