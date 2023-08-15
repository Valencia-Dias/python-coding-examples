a = 1234
rev_num = 0

# 1. Using mod
while a != 0:
    digit = a % 10
    rev_num = rev_num * 10 + digit
    a //= 10

print("Reversed number", rev_num)

# 2. Using string slicing
c = 234
b = str(c)
print("Reversed number using string slicing", b[::-1])