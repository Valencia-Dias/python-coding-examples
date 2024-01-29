def max_occurrence(s):
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    max_value=max(d.values())
    for i,j in d.items():
        if j==max_value:
            print("The charcter occuring with maxiumum count is- ", i, "and count is", j)


max_occurrence("valaaaaabl")

