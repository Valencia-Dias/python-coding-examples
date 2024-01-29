d = {'Riya': 23, 'Tina': 4, 'Sheena': 65}
k = d.keys()
print(k)
for i in k:
    print(i)

for j in d.values():
    print(j)

for k, v in d.items():
    print(k, v)


# Checking the type
print(type(d.keys()))
print(type(d.values()))
print(type(d.items()))
