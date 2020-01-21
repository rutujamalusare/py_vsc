fname = input("enter first name=")
lname = input("enter last name=")
print(f"before swapping = {fname} and lname = {lname}")

fname,lname=lname,fname
print(f"after swap fname = {fname} lname = {lname}")