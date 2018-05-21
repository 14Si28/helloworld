'''
Program to Find Numbers Divisible by Another Number
The function filter(function, list) filters out all the elements of a list, for which the function function returns True.
The function filter(f,l) needs a function f as its first argument. f returns a Boolean value,
i.e. either True or False. This function will be applied to every element of the list l.
Only if f returns True will the element of the list be included in the result list.
'''

import random as r
c = []
for i in range(1,21):
    c.append(r.randint(1,50)) #Storing the random generated values in the list.
print(c,end=" ")
n = int(input("\nEnter the divisor: "))
lambda_func = list(filter(lambda i: (i%n == 0), c))
print("The numbers divisible by {0}, is: {1}".format(n,lambda_func))