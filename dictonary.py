'''
Dictionaries can be contained in lists and vice versa.
Dictonaries are presented using {} (curly braces)
Lists are ordered sets of objects, whereas dictionaries are unordered sets.
But the main difference is that items in dictionaries are accessed via keys and not via their position.
A dictionary is an associative array (also known as hashes).
Any key of the dictionary is associated (or mapped) to a value.
The values of a dictionary can be any Python data type.
So dictionaries are unordered key-value-pairs.

Dictionaries don't support the sequence operation of the sequence data types
like strings, tuples and lists. Dictionaries belong to the built-in mapping type.
They are the sole representative of this kind!
'''

dict={'EA':105.31,'HAWK':34.50, 'BIDU':41.74}
dict1={'EA':[105.31,'Buy'],'HAWK':[34.50,'sell'], 'EA':[41.74,'Buy']}
print(dict)
print(dict['EA'])
dict['ADIDAS']= 100  # In this way we add the data into out dictonary
print(dict)
dict['ADIDAS']=101 # Altering the data
print(dict)
del dict['ADIDAS'] # In this way we delete the data from our dictonary
print(dict)
print(dict1['EA']) # Here it will always fetch data from the right most if duplicated
dict1['EA']=100,"Sell"
print(dict1) #And it removes the data left sided from the dictonary
