a = [3, 2, 7, 9, 1, 4]
temp = a[0]
a[0] = a[-1]
a[-1] = temp
print(a)

# use the comma operator
b = [3, 2, 7, 9, 1, 4]
b[0], b[-1] = b[-1], b[0]
print(b)

# using pop
c = [3, 2, 7, 9, 1, 4]
first = c.pop(0)
last = c.pop(-1)
c.insert(0, last)
print(c)
c.append(first)
print(c)
