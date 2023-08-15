x = lambda a, b: a + b
print('Result is ', x(1, 3))

s = 'welcome'
convert_upper = lambda s1: s1.upper()
print('Converted string is ', convert_upper(s))

a = lambda x: x * x * x
print('Cube is ', a(2))

# lambda  using if else
y = lambda a, b: a if a > b else b
print( str(y(2, 4)) + ' is greater')
