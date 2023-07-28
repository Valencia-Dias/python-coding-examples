# s = 'dias'
# s1 = list(s)
# a = ''
# print(s1)
# for i in range(len(s1)):
#     a += s1[i].pop()
#     print(a)
#     print('a-', a)
#
# print(a)
#

s = 'dias'
a = ''
for i in s:
    a = i + a
    print(a)
    print('a-', a)

print(a)


