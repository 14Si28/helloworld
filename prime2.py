'''Program to check the entered number is a prime number or not'''
import math
n = input("Enter the number: ")
n = int(n)
if (n == 1 or n==0):
    print("Its neither prime nor composite")
else:
    for i in range(2,n): # Need to improve efficiency int(math.ceil(n/2) and not giving o/p for 2
        if(n%i == 0):
            print(n,": is not a prime number")
            break
        else:
            print(n,": is a prime number")
            break