'''Program to check the given year is a leap year or not
leap year condition used:
leap year if: given year is divisible by 4, if then 100 then 400

2017 is not a leap year
1900 is a not leap year 4 100
2012 is a leap year     4
2000 is a leap year     4  100 400
'''

y = input("Enter the year: ")
y = int(y)
if (y%4 == 0):
    if (y%100 == 0):
        if (y%400 == 0):
            print(y,": is a leap year")
        else:
            print(y,": is not a leap year")
    else:
        print(y,": is a leap year")
else:
    print(y,": is not a leap year")