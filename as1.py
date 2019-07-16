
import re

def add(a,b):
    x = int(a)
    y = int(b)
    sum=x + y
    return sum


def sub(a, b):
    x = int(a)
    y = int(b)
    sub = x - y
    return sub

def mul(a, b):
    x = int(a)
    y = int(b)
    mul = x * y
    return mul

def div(a, b):
    x = int(a)
    y = int(b)
    div = x / y
    return div


s = input("Enter string\n")
if re.match("(\d*\D*)+\+(\d*\D*)+-(\d*\D*)+", s):
    l=list()
    l=re.findall(r'[0-9]+',s)
    m = add(l[0], l[1])
    z=sub(m,l[2])
    print(z)
elif re.match("(\d*\D*)+\+(\d*\D*)+\+(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = add(l[0], l[1])
    z = add(m, l[2])
    print(z)

elif re.match("(\d*\D*)+-(\d*\D*)+\+(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = sub(l[0], l[1])
    z = add(m, l[2])
    print(z)
elif re.match("(\d*\D*)+\*(\d*\D*)+\+(\d*\D*)+", s) :
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = mul(l[0], l[1])
    z = add(m, l[2])
    print(z)

elif re.match("(\d*\D*)+\*(\d*\D*)+-(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = mul(l[0], l[1])
    z = sub(m, l[2])
    print(z)

elif re.match("(\d*\D*)+\+(\d*\D*)+\*(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = mul(l[1], l[2])
    z = add(m, l[0])
    print(z)
elif re.match("(\d*\D*)+-(\d*\D*)+\*(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = mul(l[1], l[2])
    z = sub(m, l[0])
    print(z)

elif re.match("(\d*\D*)+/(\d*\D*)+\+(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = div(l[0], l[1])
    z = add(m, l[2])
    print(z)

elif re.match("(\d*\D*)+/(\d*\D*)+-(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = div(l[0], l[1])
    z = sub(m, l[2])
    print(z)

elif re.match("(\d*\D*)+\+(\d*\D*)+/(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = div(l[1], l[2])
    z = add(m, l[0])
    print(z)
elif re.match("(\d*\D*)+-(\d*\D*)+/(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = div(l[1], l[2])
    z = sub(m, l[0])
    print(z)

elif re.match("(\d*\D*)+\*(\d*\D*)+/(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = mul(l[0], l[1])
    z=div(m,l[2])
    print(z)

elif re.match("(\d*\D*)+/(\d*\D*)+\*(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = div(l[0], l[1])
    z = mul(m, l[2])
    print(z)

elif re.match("(\d*\D*)+-(\d*\D*)+",s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = sub(l[0], l[1])
    print(m)

elif re.match("(\d*\D*)+\+(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = add(l[0], l[1])
    print(m)

elif re.match("(\d*\D*)+\*(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = mul(l[0], l[1])
    print(m)

elif re.match("(\d*\D*)+/(\d*\D*)+", s):
    l = list()
    l = re.findall(r'[0-9]+', s)
    m = div(l[0], l[1])
    print(m)



else:
    print("false")
