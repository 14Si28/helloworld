'''
Program To Display Powers of 2 Using lambda Function
'''

lambda_func = lambda n: 2**n
n = int(input("Enter till which term 2 power to be calculated: "))
for i in range(1,n+1):
    print("2 power {0} is = {1}".format(i,lambda_func(i)))