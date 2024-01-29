# do  not change this function first sub()...

def sub(a, b):
    print(a - b)


def sub_decorator(func):
    def inner_function(a, b):
        if a < b:
            a, b = b, a
        return sub(a, b)

    return inner_function


sub1 = sub_decorator(sub)
sub1(2, 9)
