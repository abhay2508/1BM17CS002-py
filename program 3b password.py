from random import shuffle
import string

chars=string.ascii_letters+string.punctuation+string.digits
characters=[]
for char in chars:
    characters.append(char)
shuffle(characters)
length=int(input("enter the length of the password"))
password=' '
for i in range(length):
    password+=characters[i]
print(password)
