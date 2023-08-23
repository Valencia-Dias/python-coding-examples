# 1. Using for loop
s = 'hello'
s1 = ''
for i in range(len(s)):
    if i == 0 or i == len(s) - 1:
        s1 = s1 + s[i].upper()
    else:
        s1 = s1 + s[i]
print(s1)

# 2. Without for loop
a = 'welcome'
first = a[:1].upper()
second = a[len(a) - 1:].upper()
other = a[1:len(a) - 1]
print("Final string ", first + other + second)
