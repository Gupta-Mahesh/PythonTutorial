
#And, OR and Not operator is going to use

a = 10
b = 20
c = 30

print('and:- both should be true: a<b and b<c:', a < b and b < c)

print('or: a<b or b>c:', a < b or b > c)

print("Not:", a!=b)
print('not: a>b:',not a > b)

print()
s1 = ''
s2 = s1 or 'defaultStr'
print("In case of false (Empty String), default value taken s2:", s2)

l1 = []
l2 = l1 or [1, 2, 3]
print("In case of true, default value taken l2:", l2)

print()

x = 10
print(" x or 30: ", x or 30)  # in "or" if 1st value is true, 2nd not considered

y = 0
print("y or 30", y or 30)  # 

z = 40
print(" z and 50:", z and 50)  # in "and" value till last is considered,

z = 0
print(" z and 50:", z and 50)  # in "and" value till last is considered,


# Python program to demonstrate
# order of evaluation of logical 
# operators

def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False
    
a = order
b = order
c = order

if a(1) and b(-5) | c(10):
    print("Atleast one of the number is positive")


print(5%20)
print((4+5)*5**(4-2))
str="GFG"
print(not(not(str and "")))
s="gfg"
print("G" in s)
print(("g" or "")in s)
print(not("g" or "")not in s)
print(oct(23)+oct(23))

