class dog:
    def speak(self):
        print("Bow Bow")

class cat:
    def speak(self):
        print("Meow Meow")

class duck:
    def speak(self):
        print("Quack Quack")

def speak(animal):
    animal.speak()

def all_speak(object):
    object.speak()

x = dog()
all_speak(x)