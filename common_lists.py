data_1 = [45,2,6,87,12,94,78,23,90,11,49,78,99]
data_2 = [[94, 17, 18, 234, 43], [7, 19, 87, 18, 36], [11, 45, 80, 99]]

# Map applies a function to all the items in an input_list
o1 = [list(map(lambda n: n in data_1, store_in)) for store_in in data_2]
print(o1)

# Filter creates a list of elements for which a function returns true
o1 = [list(filter(lambda n: n in data_1, store_in)) for store_in in data_2]
print(o1)

