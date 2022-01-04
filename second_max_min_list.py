# Find the second max and second min
a=[11,1,22,34,3,55,2,4,1,90,2,4,8,55,67,89,98,3]
set1=set(a)
print(set1)
l=list(set1)
print(l)
l.sort()
print(l)
print("Second max is: ",l[-2] )
print("Second min is: ",l[1] )
