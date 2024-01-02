x=5
def test():
    x=4
    print(x)
test()
print(x)


x = "global"
def foo():
 global x
 x = 'Global'
foo()
print(x)
