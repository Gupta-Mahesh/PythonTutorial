
# Comparing literals
a=10
b=10
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
print(a==b)
print(a!=b)

if a is not b:
    print("Sahi Jawab a b ke barabar nahi hai")
elif a is b:
    print("Sahi Jawab a b ke barabar hai")
else:
    print("Galat Jawab")


# Comparing collections
print()
c=[1,2,3,4]
d=[5,6,7,8]
print(c is d)
print(c is not d)
print(id(c))
print(id(d))

print()
e=[1,2,3,4]
f=[1,2,3,4]
print(e is f)
print(e is not f)

print()
g=[12,13,14,15]
h=g
print(g is h)
print(g is not h)
print(id(g))
print(id(h))
