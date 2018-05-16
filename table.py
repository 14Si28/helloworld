'''
Program to print the multiplication of a number till its square(Result)
'''
n = input("Enter the number: ")
n = int(n)
for i in range(1,n+1): # Since for loop will break at n+1 and we are calculating till n, hence n+1
    print(n, " * ", i, " = ", n*i)