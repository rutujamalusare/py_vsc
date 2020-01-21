mylist=[1,2,3,4]

print(mylist)
#del mylist
#print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist = thislist
print(mylist)

print(id(mylist))
print(id(thislist))