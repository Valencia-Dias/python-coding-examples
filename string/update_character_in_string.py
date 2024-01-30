s = "welcome"
#1. update second letter to o
#Strings are immutable, hence use a list and than convert to a string

l = list(s)
l[1] = "o"
print('String : ', "".join(l))

# 2. Convert first letter to uppercase and last to small case
st = "diaS"
st1 =""
st1 = st[0].upper()+st[1:-1] +st[-1].lower()
print("Updated " +st1)

