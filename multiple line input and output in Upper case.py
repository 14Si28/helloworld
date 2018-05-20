lines = []
while True:
    s =input("Enter the string or ENTER for Output: ")
    if s:
        lines.append(s.upper())
    else:
        break;

print("OUTPUT in Upper Case: ")
for i in lines:
    print (i)
