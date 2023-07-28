def checkElement(element):
    a = [2, 1, 4, 9, 1, 22, 45]
    for i in a:
        if i == element:
            return 'Element found', element


def checkElementNotInList(element):
    b = [2, 1, 4, 9]
    for i in b:
        if i != element:
            return 'Element not found'


def checkElementUsingIn(element):
    a = [2, 1, 4, 9, 1, 22, 45]
    if element in a:
        return 'Element found', element


def checkElementUsingNotIn(element):
    a = [2, 1, 4, 9, 1, 22, 45]
    if element not in a:
        return 'Element not found'


print(checkElement(9))
print(checkElementNotInList(3))
print(checkElementUsingNotIn(8))
print(checkElementUsingIn(2))
