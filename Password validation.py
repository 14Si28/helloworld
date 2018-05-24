import re
value = []
items=input("Enter the password for validation (comma seperated): ").split(',')
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    elif not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    else:
        value.append(p)
print (",".join(value))