amount=0
while (True):
    i=input("Enter amount prefixed by d/D (deposit) or w/W (withdrawal) or e/E (Exit): ").split(" ")
    if (i[0]=='D' or i[0]=='d'):
        amount+=int(i[1])
    elif (i[0]=='W' or i[0]=='w'):
        amount-=int(i[1])
    elif (i[0]=='e' or i[0]=='E'):
        print("Total amount %d" % amount)
        break
    else:
        print("Wrong input !!!")
        break