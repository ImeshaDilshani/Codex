import mymodule 

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = dir(platform)
print(x)