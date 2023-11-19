#guessing the number
'''computer has a number we have to guess it'''

from random import randint as rint
def user_guess():
    x = rint(0,101)
    c = int(input("tell number from 0 to 100 \n"))
    while x>-1:
        if c<x:
            c = int(input("try larger number\n "))
        elif c>x:
            c = int(input("try smaller number\n  "))
        else:
            print(f"you got it the number was {c} ")
            break
#user_guess()
def computer_guess():
    x = int(input("enter the number so that computer can guess? \n"))
    c = rint(0,101)
    while x!=c:
        c=rint(0,101)
        print(c)
    print(f"the number was {c}")

computer_guess()