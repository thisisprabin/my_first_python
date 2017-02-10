data1=[1,2,3,4];
data2=['x','y','z'];
print(data1[0])
print(data1[0:2])
print(data2[-3:-1])
print(data1[0:])
print(data2[:2])

list1=[10,20]
list2=[30,40]
list3=list1+list2
print(list3)

data1=[5,10,15,20,25]
print("Values of list are: ")
print(data1)
data1[2]="Multiple of 5"
print("Values of list are: ")
print(data1)

list1=[10,"rahul",'z']
print("Elements of List are: ")
print(list1)
list1.append(10.45)
print("List after appending: ")
print(list1)

list1=[10,'rahul',50.8,'a',20,30]
print(list1)
del list1[0]
print(list1)
del list1[0:3]
print(list1)


#Functions and Methods of Lists

list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print("Minimum value in List1: ",min(list1))
print("Minimum value in List2: ",min(list2))

list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print("Maximum value in List : ",max(list1))
print("Maximum value in List : ",max(list2))

list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
print("No. of elements in List1: ",len(list1))
print("No. of elements in List2: ",len(list2))

list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
list3=[101,981,'abcd','xyz','m']
print(cmp(list1,list2))
print(cmp(list2,list1))
print(cmp(list3,list1))





