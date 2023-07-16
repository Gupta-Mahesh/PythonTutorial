
# general purpose functions

list1 = [10, 40, 20, 50]

print(list1)

print('max', max(list1))

print('min', min(list1))

print('sum', sum(list1))

list1.reverse()

print('after reverse', list1)

list1.sort()

print('after sorting', list1)

#Example 2: Even list using list comprehension
print("\nEven: ")
list = [i for i in range(11) if i % 2 == 0]
print("Even List: ",list)

#Example 3: Matrix using List comprehension
print("\nMatrix: ")
matrix = [[j for j in range(10,15)] for i in range(3)]
   
print(matrix)


print("\n\n")
my_string="geeks"
k=[(i.upper(),len(i))for i in my_string]
print(k)

print("\n")
print([i.lower() for i in "GFG"])

print("\n")
s=["GEEKS","FOR","GEEKS"]
k=[(w.lower(),len(w)) for w in s]
print(k)

#t=32.00
#[round((x-32)*5/9)for x in t]


c=[(1,2,4),(5,6,7),(8,9,10)]

t=(2,3,4,5)
print(sum(t,3))
print("\n")
a={4,5,6}
b={2,8,6}
print(a-b)

s=set()
print(type(s))

l=[1,2,3,4,5,6,7,8,9]
l1=[x**3 for x in l]
print(l1)