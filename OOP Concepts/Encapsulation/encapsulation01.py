class A:
    def __init__(self):
        self.__var = 123

    def __display(self):
        print("Display methods of A class")

    def printVar(self):
        self.__display()
        print(self.__var)

x = A()
x.printVar()