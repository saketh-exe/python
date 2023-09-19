'''Problem 2: Write a Python program to check if a given string is a palindrome.'''


word = input("what is the word ? ").lower()
a = 0
b = len(word) - 1
c = 0
while b >= a :
    q = word[a]
    w = word[b]
    if q != w :
        c += 1
        break
    b -= 1
    a += 1
   
if c > 0:
    print("the word is not a plaindrome") 
else:
    print("it's a plaindrome")   
    



