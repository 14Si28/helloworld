print("Program to calculate the values of the quadratic equation ax^2+bx+c=0")
a = input("Enter the value of a: ")
a = int(a)
b = input("Enter the value of b: ")
b = int(b)
c = input("Enter the value of c: ")
c = int(c)
#calculating the discriminant first then the roots
d = b*b - 4*a*c
if (d > 0):
    d = d**0.5
    print("\nThe roots are real")
    x1 = (-b+d)/2*a
    x2 = (-b-d)/2*a
    print("The roots are: {0}, {1} ".format(x1,x2))
else:
    print("\nThe roots are imaginary")