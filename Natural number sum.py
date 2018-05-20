'''
Program to calculate the sum of natural numbers.
Natural numbers are from 1 and above.
'''
l = int(input("Enter till which number you want the sum: "))
sum = 0
if (l>0):
    for i in range(1,l+1):
        sum += i
    print("The sum of numbers are: ",sum)
else:
    print("Invalid range!!!")