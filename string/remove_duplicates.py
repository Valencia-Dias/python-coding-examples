# 1. Remove duplicates from a string using set-
# Note- not maintaining the order here
s = 'adab'
s1 = set(s)
final_string = ''
for i in s1:
    final_string += i

print('String without duplicates without maintaining the order ', final_string)



# 2. Remove duplicates from a string
# Note- Maintaining the order here
s1 = 'adab'
s2 = ''
for i in s1:
    if i not in s2:
        s2 += i

print('String without duplicates with the same order of alphabets- ', s2)
