#Python code for sorting without using sort

a = [11, 2, 3, 4, 15, 6, 7, 8, 9, 10]
print("Original list :-",a)
for i in (0,len(a)):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a1=a[i+1]
            a[i+1]=a[i]
            a[i]=a1
print("Sorted list:-",a)


