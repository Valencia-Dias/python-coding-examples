a=[2,4,5,9,1]
b=[3,5,6,1,8,9]
c=[2,34,1.5,23,56,6,78,4]
d=["Val","Sam","Dan","Shreya","Dave","Ben"]
e=[1,2,3]
print("List a:-",a)
print("List b:-",b)
print("List c:-",c)
print("List d:-",d)
print("List e:-",e)
#1. Length of a list
print("The length of list a is ",len(a))
print("The length of list b is ",len(b))
#2. Sorting a list
c.sort()
print("The sorted list c is- ",c)
d.sort()
print("The sorted list d is- ",d)
#3. Find the type
print("Type of c is:-",type(c))
print("Type of d is:-",type(d))
#4. Append to a list
a.append(6)
print("Element appended to the list ",a)
#5. Extend
a.extend(e)
print("List a after extend is ",a)
#6. Index of a list
print("Index  of element 6 from a:-",a.index(6))
#7. Find maximum in a list
print("Maximum from list C is-",max(c))
#8. Find minimum in a list
print("Minimum from list C is-",min(c))
#9 Sum of elements in a list
print("Sum of elements in E:-",sum(e))
#10. Compare 2 lists
set1=set(a)
set2=set(b)
if a == b:  #or a==b
    print("The list1 and list2 are equal")  
else:  
    print("The list1 and list2 are not equal")  
# 11. Clear a list
list2=[11,2,16,2,3,90]
print("List2 is:-",list2)
print("List after clearing:-",list2.clear())
#12. Copy a list
veg = ["tomato", "onion", "okra"]
veg_copy= veg.copy()
print("Copy of list is:-",veg_copy)
#13. Find count of a specific element in a list
vehicles = ["car", "bike", "car"]
x = vehicles.count("car")
print("Count of car is:-",x)

#14. Remove an element from a list
string1 = ['abc', 'xyz', 'pqr']
string1.remove("xyz")
print("List after removing:-", string1)

#15. Pop an alement
string2 = ['cat', 'dog', 'horse','parrot']
string2.pop()
print("List after pop():-",string2)
string2.pop(1)
print("List after pop(1):-",string2)
#16. Reverse a list
string2.reverse()
print("Reversed above list:-",string2)

# 17.Insert
string3 = [31, 2,11,7,89]
string3.insert(1,4)
print("List after inserting a new element",string3)

