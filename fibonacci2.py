'''
Fibonacci series is the integer sequence of 0,1,1,2,3,5,8,13... and so on.
'''
def fibonacci(n):
    a = 0
    b = 1
    if(n>2):
        print(a,b, end=" ") # using end=" ", to tell compiler not to go in new line.
        for i in range(2,n):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
    elif (n == 2):
        print(a,b)
    elif (n == 1):
        print(a)
    elif(n<0 or n==0):
        print("No values")


n = int(input("Enter the number of the terms: "))
fibonacci(n)