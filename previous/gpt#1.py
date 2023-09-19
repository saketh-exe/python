# this is loop method 
num = int(input("Enter number ?\n"))
y= 1
for x in range(1,num+1):
    y=y*x
print("factorial of num",y)  
''' first we define a variable as 1 because the calculation of factorial is from 1 to n 
and when it enters inside loop fist y will be like 1*1 and this takes the value of y and 
second step will be like 1*2 here only illration variable changes with loop and the multiplied value gets used in 
next step of loop ''' 



'''there is other way of doing this "recursion" method '''
'''so basically waht happens as name suggests the function "factorial" just repeats it self everytime 
with new number 
firstly in this the multiplication starts from back and each time one number gets reduced and multiplied 
to previous number'factorial'''

def factorial(n):

    if n == 0 :# base step
        return 1
    else:# recursive step 
        return n*factorial(n-1)
    
result = factorial(num)
print(result)