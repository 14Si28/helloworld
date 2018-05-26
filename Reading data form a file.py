readMe=open('FileName.txt', 'r').read()
print(readMe)

readMe=open('FileName.txt','r').readlines() #reading the file line wise and storing in list
print(readMe)

readMe=open('FileName.txt','r').read().split() #reading the file word wise and then storing in the list.
print(readMe)