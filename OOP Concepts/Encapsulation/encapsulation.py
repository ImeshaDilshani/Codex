# class myClass:
#     x = 5
#     __y = 10

# myObject = myClass()
# print(myObject.x)
# print(myObject._myClass__y) # This is how you access private variables in Python

class myClass:
    def meth1(self):
        print("myClass meth1")
        self.__meth2()

    def __meth2(self):
        print("myClass meth2")

myObject = myClass()
myObject.meth1()
# myObject.__meth2() # This will cause an error

