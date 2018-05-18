list_a= [2,4,5,7,9,0] # Only list is represented using square brackets.
tuple_a=(2,3,4,5,6,7) # Tuple is represented using first brackets.
# In list we can do the modification but the tuple is a constant list, and a list can contain a set of tuples
list_b=[(2,3),(4,3),(5,8)]
print(list_a)
list_a.append(23)
print(list_a)
print(tuple_a)
#tuple_a.append(34) # This will result in an error
print(list_b)
list_b.append((3,2))
print(list_b)