import re
str=input("enter string\n")
print("number of characters in string is ",len(str))
l=[]
u=0
lo=0
s=0
if str.isdigit():
    print(str," is integer")
    str1=int(str)
    if str1%2==0:
        print(str," is even")
    else:
        print(str," is odd")
    l=list(str)
    tot=0
    for i in range(0,len(l)):
        tot=tot+int(l[i])
    print("the sum of digits is ",tot)

elif str.isalpha():
    print(str," is string")
    if str.isupper():
        print("all letters are in upper case")
    elif str.islower():
        print("all letters are in lower case")
    else:
        print("letters are in both upper and lower case")
    for i in str:
         if i.isupper():
             u=u+1
         elif i.islower():
             lo=lo+1
    print("the number of uppercase letters are ",u)
    print("the number of lowercase letters are ",lo)


elif str.isalnum():
    print(str," is alphanumeric")



elif re.match("[-+]?([0-9]*\.[0-9]+|[0-9]+)", str):
    print(str," is float")

elif re.match("[a-zA-Z0-9_]*$", str):
    pass
else:
    print(str," contains special characters")
    for i in str:
        if i.isalpha():
            continue
        else:
            s=s+1
    print(" contains ",s," special characters")