# python 1
# basic data types

h = "hello"
w = "world"

print(h,w)
print(h+w)

n1 = '5'
print(h+n1)

# how to concatenate str with number?
# typecasting

print(h+str(n1))

multilinestring = """
    str() - cast to string
    int() - cast to integer
    float() - cast to float
"""

print(h+str(n1))

# formatted strings
n1 = 5 
n2 = 3
res = n1 +n2
out = f"{n1}+{n2}={n1+n2}"
print(out)

# logical operators
# code block

n1 = 5
n2 = 3

if n1<n2:

    print("lesser")
    print("<"*6)

elif n1==n2:
    print("equal")
    print('====') 

else: 
    print("greater")
    print(">"*len("greater"))


# blocks in python use indentation
# used in if statements/function def

f = 17.4
print(type(f))
