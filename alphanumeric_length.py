s=input("Enter the string: ")
small_letter=0
capital_letter=0
digits=0
space=0
others=0
x=len(s)
for i in range(0,x,1):
    if ((ord(s[i]) >= 97) and (ord(s[i]) <= 122)):
        small_letter=small_letter+1
    elif ((ord(s[i]) >= 65) and (ord(s[i]) <= 90)):
        capital_letter+=1
    elif ((ord(s[i]) >= 48) and (ord(s[i]) <= 57)):
        digits+=1
    elif (ord(s[i])==32):
        space+=1
    else:
        others+=1
print("small letter: %d \n capital letter: %d \n digits: %d \n space: %d \n others: %d \n" %(small_letter,capital_letter,digits,space,others))