print("_____________________int_________________________")
a=90
print(a)
print(type(a))
print(float(a))
print(complex(a))
print(bool(a))
print(str(a))
#print(list(a)) 
#TypeError: 'int' object is not iterable
#print(tuple(a))
#TypeError: 'int' object is not iterable
#print(dict(a))
#TypeError: 'int' object is not iterable
#print(set(a))
#TypeError: 'int' object is not iterable
print("____________________float_________________________")
#float data type
b=9.908
print(b)
print(type(b))
print(int(b))
print(float(b))
print(complex(b))
print(bool(b))
print(str(b))
#print(list(b))
#TypeError: 'float' object is not iterable
print("_________________complex_____________________")
#complex data type
c=90+0j
print(c)
print(type(c))
#print(int(c))
#TypeError: can't convert complex to int
#print(float(c))
#TypeError: can't convert complex to float
print(complex(c))
print(bool(c))
print(str(c))
print("________________bool_____________________")
#boolean data type
d=True
print(int(d))
print(float(d))
print(complex(d))
print(bool(d))
print(str(d))
#print(list(d))
#TypeError: 'bool' object is not iterable
print("____________________str________________________")
e="rutuja"
print(e)
print(type(e))
#print(int(e))
#print(float(e))
#print(complex(e))
print(bool(e))
#if string is empty bool of str will be false
f=""
print(f)
print(bool(f))

