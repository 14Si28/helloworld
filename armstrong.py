s = int(input("Enter the start: "))
e = int(input("Enter the end: "))
for i in range(s,e+1):
    sum = 0
    l = len(str(abs(i)))
    temp = i
    for j in range(1,l+1):
        sum += (temp%10)**l
        temp = int(temp/10)
    if(sum == i):
        print("The Armstrong number: ", i)
