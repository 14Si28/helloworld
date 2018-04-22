x=int(input("enter the row: "))
y=int(input("enter the column: "))
for i in range(0,x,1):
    for j in range(0,y,1):
        print(i*j,' ', end="")
    print("\n")