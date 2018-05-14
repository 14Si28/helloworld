'''
Power using lambda function
'''

lambda_func = lambda x,y: x**y
x = int(input("Enter the number: "))
y = int(input("Enter the power: "))
print("Value: ",lambda_func(x,y))