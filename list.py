list_a=[1,3,6,8,0,3,98,5,8,3,2,4,6]
list_a.insert(2,99) # this will insert the 99 to the 2nd index i.e. the 3rd element.
print(list_a)
list_a.remove(list_a[5]) # Will remove 0
print(list_a)
print(list_a[2:5]) # Will give 2nd, 3rd, 4th element
print(list_a[-1]) # will give the last element
print(list_a.index(98)) # this will give the index value for the first element/number i.e 98
print(list_a.count(2)) # this will count the number of 2's in the list
list_a.sort() # This will sort the list, in ascending order (if names then alphabetically)
print(list_a)