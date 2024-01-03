class Student:
    def __init__(self, student_id, student_name):
        self.__id = student_id  # Private variable
        self.__name = student_name  # Private variable

    def display(self):
        print(f"Student ID: {self.__id}")
        print(f"Student Name: {self.__name}")

    def learn(self):
        self.__learn()  # Call the private method

    def modify(self, new_id, new_name):
        self.__id = new_id
        self.__name = new_name

    # Private method
    def __learn(self):
        print(f"{self.__name} is learning.")

# Creating an instance of the Student class
student1 = Student(student_id=1, student_name="John Doe")

# Displaying initial information
print("Initial Information:")
student1.display()

# Modifying information from outside the class
student1.modify(new_id=2, new_name="Jane Doe")

# Displaying modified information
print("\nModified Information:")
student1.display()

# Calling the learn method
print("\nCalling the learn method:")
student1.learn()
