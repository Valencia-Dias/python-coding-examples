a = [1, 2, 3, 4, 5, 6, 2, 4, 7]
k = 3
# a = [5, 4, 1, 2, 3]
# index = (i +2 ) % len(a)
# shift right by k =2


# method 1-reverse the array and than apply reverse on each sub array O(1)
a.reverse()
b = a[:k]
c = a[k:]
b.reverse()
c.reverse()
print(b, c)
print(b + c)


#method 2
k = k % len(a)


