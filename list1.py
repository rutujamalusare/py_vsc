a=[[1,2,3,[11,22,33,[1.1,2.2,3.3]]]]
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[0][3][0])
print(a[0][3][1])
print(a[0][3][2])
print(a[0][3][3][0])
print(a[0][3][3][1])
print(a[0][3][3][2])

cities=list(("pune","mumbai"))
print(cities)
cities.append("satara")
print(cities)

cities[1]="nagpur"
print(cities)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

