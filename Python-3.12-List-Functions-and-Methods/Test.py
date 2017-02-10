list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print("No. of elements in List1: ",len(list1))
print("No. of elements in List2: ",len(list2))

data = [786,'abc','a',123.5]
print("Index of 123.5:", data.index(123.5))
print("Index of a is", data.index('a'))

data = [786,'abc','a',123.5,786,'rahul','b',786]
print("Number of times 123.5 occured is", data.count(123.5))
print("Number of times 786 occured is", data.count(786))

data = [786,'abc','a',123.5,786]
print("Last element is", data.pop())
print("2nd position element:", data.pop(1))
print(data)

data=['abc',123,10.5,'a']
data.insert(2,'hello')
print(data)

data1=['abc',123,10.5,'a','xyz']
data2=['ram',541]
print(data1)
data1.remove('xyz')
print(data1)
print(data2)
data2.remove('ram')
print(data2)

list1=[10,20,30,40,50]
list1.reverse()
print(list1)


