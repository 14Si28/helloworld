out=[]
start_end=input("Enter the range start and end value seperated by comma, such that Start is smaller than end value: ").split(",")
print(start_end[0],start_end[1])
temp=0
for i in range(int(start_end[0]),int(start_end[1])+1,1):
    a=str(i)
    x=i
    for j in range(0,len(a),1):
        y=x%10
        if y%2==0:
            temp=1
        else:
            temp=0
            break
        x=int(x/10)
    if temp==1:
        out.append(i)
print("The values whose digits are divisible by 2 are: ", out)