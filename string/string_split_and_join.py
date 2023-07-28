def stringSplit(s1):
    a = s1.split()
    b = []
    for i in a:
        j = i[::-1]
        b.append(j)
    s1 = " ".join(b)
    return s1


s = 'welcome to abc'
print(stringSplit(s))
