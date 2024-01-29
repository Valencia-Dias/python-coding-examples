def sort_ascending(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            # print(a[i])
            # print(a[j])
            if a[i] > a[j]:
                (a[i], a[j]) = (a[j], a[i])
    return a


def sort_descending(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                (a[i], a[j]) = (a[j], a[i])
    return a


print("Ascending list", sort_ascending([4, 2, 8, 1]))
print("Descending list",sort_descending([4, 2, 8, 1]))
