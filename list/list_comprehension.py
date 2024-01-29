# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.
#Example 1
vehicles = ['bikes', 'cars', 'trucks', 'buses']
vehicles_new_list = [i for i in vehicles if i == 'buses']
print(vehicles_new_list)

#Example 2
color = ['red', 'blue', 'green', 'black']
colors_new_list = [i for i in color if 'e' in i]
print(colors_new_list)

#Example 3
a = [1, 'a', 'abc', 5]
b = [x for x in a]
print(b)

#Example 4
a =['VD', "AB"]
c = [x.lower() for x in a]
print(c)