class myClass:
    x = 5
    __y = 10

myObject = myClass()
print(myObject.x)
print(myObject._myClass__y) # This is how you access private variables in Python