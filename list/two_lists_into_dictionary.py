a = [1, 2]
b = ['a', 'b']
d = {}

# 1. without update()
for i in range(len(b)):
    d[b[i]] = a[i]
print(d)

# 1. with update()
c = {}
for i in range(len(b)):
    c.update({b[i]: a[i]})
print(c)
