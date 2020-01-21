no1= input("enter 1st number")
no2= input("enter 2nd number")

operation= input("enter operation to be performed")
if (operation ==sum):
    sum = float(no1) + float(no2)
    print('The sum of {0} and {1} is {2}'.format(no1, no2, sum))
else:
    pass

#subtraction
sub = float(no1) - float(no2)
print('The subtraction of {0} and {1} is {2}'.format(no1,no2,sub))

#multiplication
mul = float(no1) * float(no2)
print('The multiplication of {0} and {1} is {2}'.format(no1,no2,mul))

#division
div = float(no1) / float(no2)
print('The division of {0} and {1} is {2}'.format(no1,no2,div))


 


