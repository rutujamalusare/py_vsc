
"""
numbers=[1,2,3,1+10j,'one','two','three',True,False,[1,2,3]]
print(numbers)
print(f"lenth={len(numbers)}")

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

numbers[4]=1
print(numbers[4])

for n in numbers:
    print(n)

print(numbers[0:1])    #accesing list element by slicing
print(numbers[1:2])
print(numbers[2:3])
print(numbers[3:4])
print(numbers[-1:10])
"""

#multidia list

list=[[1,2,3],[4,5,6]]
print(list)
print(list[0])
print(list[0][0])
a=(list[0][0]+list[1][0])
b=(list[0][0]+list[1][0])
c=(list[0][2]+list[1][2])



print(list[0][0]+list[1][0])
print(list[0][1]+list[1][1])
print(list[0][2]+list[1][2])

f=[a,b,c]
print(f)

f=(a,b,c)
print(list(f))

