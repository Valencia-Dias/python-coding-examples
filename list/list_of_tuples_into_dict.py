a = [(2, 1), (3, 4)]
b = dict(a)
print(b)

# 2. Another method
d1 = {}
for k, v in a:
    print(k, v)
    d1[k] = v
print(d1)
