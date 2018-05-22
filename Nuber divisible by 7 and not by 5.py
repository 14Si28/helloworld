l=[]
for i in range(2000,3501,1):
    if (i%7==0) and (i%5!=0):
        l.append(i)
print(l)