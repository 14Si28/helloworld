w=[]
out=[]
w=input("Enter the words to be sorted alpbabetically (use comma ',' for seperation): ").split(" ")
l=len(w)
print(l)
for i in (0,l-1,1):
    for j in(i+1,l,1):
        if w[i]!=w[j]:
            out.append(w[i])            
print(sorted(out))