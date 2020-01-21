a = "Hello, World!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#retriving string character by using Index of string
print(a[0:1])
print(a[1:2])
print(a[2:3])
#using slicing
print(a[-1])
print(a[-2])
#using loop
for aa in a:
    print(aa)

#spanning string across multiple lines
line="""hello 
i am learning
python """ 
print(line) 



print(len(a))

# returns "Hello, World!"
print(a.strip()) 

print(a.lower())

print(a.upper())

print(a.replace("H", "J"))

# returns ['Hello', ' World!']
print(a.split(",")) 

a = "Hello"
b = "World"
c = a + b
print(c)

#adding space between a and b.
c = a + " " + b
print(c)

age = 36
txt = "My name is John, I am " + age
print(txt)

#format method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#escape character \is used to print ""inbetween.
txt = "We are the so-called \"Vikings\" from the north."



