s = ' I am ABC'
s1 = ''
for i in range(len(s)):
    if i+1 == " ":
        s1 = s[i] +" " + s1
    else:
        s1 = s[i] + s1
print(s1)