class French:
    def say_hello(self):
        print("Bonjour")

class Chinese:
    def say_hello(self):
        print("Ni hao")

def greeting(language):
    language.say_hello()

sarthak = French()
john = Chinese()

greeting(sarthak)
greeting(john)