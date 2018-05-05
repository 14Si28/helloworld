'''
Program to print out the factorial of the given number
say 5! = 5*4*3*2*1
'''
fact = 1
n = input("Enter the number whose factorial is to be calculated: ")
n = int(n)
if n>0:
    for i in range(n,1,-1): # Start point, Stop point, Interval
        fact *= i
    print("The factorial is : ", fact)
elif(n == 0):
    print("The factorial is: ", 1)
else:
    print("The factorial function is defined only for non negative integers")