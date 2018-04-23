'''
Armstrong numbers are of order n (positive integers):
abcd... = an + bn + cn + dn + ...
e.g. 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
'''

def armstrong(n,l):
    temp = n
    sum = 0
    for i in range(1,l+1):
        sum += (temp%10)**l
        temp = int(temp/10) # Type casting otherwise it will take float values
    print("Sum = ",sum)
    if(sum==n):
        print("It is an Armstrong number")
    else:
        print("Not an Armstrong Number")

n = input("Enter the integer number: ")
l = len(str(abs(int(n))))
print("Length = ",l)
n = abs(int(n))
armstrong(n,l)