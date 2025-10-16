import sys

class Student:
    def __init__(self, name:str,age:int):
        self.name = name
        self.age = age
    def say_hello(self):
        return f"Hello {self.name}! I am {self.age}"

stu = Student("John",20)

print(stu.say_hello())