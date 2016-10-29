class MyFirst:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    def displayName(self):
        print("Person name ", self.name)
    def displayAge(self):
        print("Person age ", self.age)
        

print("Enter the name")
name = input()
print("Enter the age")
age = int(input())

obj = MyFirst(name, age)
obj.displayName()
obj.displayAge()            