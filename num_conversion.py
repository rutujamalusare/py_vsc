no=int(input("enter number="))

print(f"binary format {no}={bin(no)}")
print(f"octal format {no}={oct(no)}")
print(f"hexadecimal format {no}={hex(no)}")

binary=(input("enter number="))
print(f"decimal format {binary}={int(no)}")

print(int(bin(no),2))

#octal to decimal to binary..
no= input("enter octal number = ")

no=bin(int(no,8))
print(f"binary = {no}")

print(f"binary = {bin(int(no,8))}") #single line code
print(f"hexadecimal = {hex(int(no,8))}")
print(f"octal = {oct(int(no,8))}")



