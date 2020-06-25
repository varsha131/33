Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #reverse a word
word=input("enter the word")
for char in range(len(word)-1,-1,-1):
           print(word[char],end="")
           print("\n")