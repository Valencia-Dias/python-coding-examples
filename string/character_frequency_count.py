a = 'aaabbbaabbdd'
# a = 'aaabc'
# output='3a3b2a2b2c'
c = 1
s = ''
st = ''
for i in range(len(a)):  # 0-12
    print(i)
    # print(a[i+1])
    if a[i+1] == a[i]:
        c += 1
    else:
        s = s + str(c) + a[i-1]
        c = 1
print(s)
