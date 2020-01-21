a="h\te\tl\tl\to"
print(a)
print(a.expandtabs(1))



import base64

string= base64.b64encode(bytes("hello  I am learning python",'utf-8'))
print(string)

string1= base64.b64decode(string)
print(string1)

string2= input("enter any string")
 
string2=base64.b64encode(bytes(string2,'utf-8'))
print(string2)

string3= base64.b64decode(string2)
print(string3)

#to remove prefix b which is printed on console.
print(string3.decode('utf-8'))

print(str(string3,'utf-8'))

