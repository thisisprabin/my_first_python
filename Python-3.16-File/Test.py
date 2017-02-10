import os

file = open("Me.txt", "w+");

print(file.name)
print("Enter the string")
str = input()
file.write(str)
file.close()

file = open("Me.txt", "r");
print(file.read())
print(file.tell())
print(file.seek(12, 0))
print(file.tell())

print("Enter the file name")
newName = input()

os.rename("Me.txt", "newName,txt")
print(file.name)

