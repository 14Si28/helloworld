inp=input("Enter the comma seperated values: ").split(",")
numbers=[x for x in inp if int(x)%2!=0]
print(",".join (numbers))