def swap_variables_arithmetic_operation(a,b):
    print("Original a and b:", a,b)
    a = a+ b #a = 7
    b = a -b # b= 3
    a = a -b
    print("After swapping a and b:", a,b)


def swap_variables_by_shifting(a, b):
    print("Original a and b:", a,b)
    a,b = b,a
    print("After swapping a and b:", a,b)


swap_variables_arithmetic_operation(3,4)
swap_variables_by_shifting(1,5)
