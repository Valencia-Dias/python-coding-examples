a = [5, 3, 2, 9, 1, 5, 0, 14]
# using sort()
a.sort()
print('largest number is ', a[-1])
print('second largest number is ', a[-2])

# Loop through the array
max1 = a[0]
for i in range(0, len(a)):
    if a[i] > max1:
        max1 = a[i]
print("Largest element in the array: " + str(max1))

# using max()
print('Largest number using max() ', max(a))
