name = "张三丰"

def mul(a,b):
    return a*b

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"