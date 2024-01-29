class Operations:

    def add_num(a, b):
        return a + b

    def show_name():
        print("Name is Valencia")


Operations.add_num = staticmethod(Operations.add_num)
Operations.show_name = staticmethod(Operations.show_name)

print(Operations.add_num(2, 3))
Operations.show_name()
