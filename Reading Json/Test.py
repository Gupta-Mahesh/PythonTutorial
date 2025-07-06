
dict={101:{"Name":"Chocholate"},
            102:"Candy",
            103:{"Roll No": 1}
            }


for key in dict.keys():
    print(key)

import numpy as np
""" arr_automatic = [1,2,3,1,4,4,7,7,8,7,8,77,88,5,44,55]
np_arr_auto = np.array(arr_automatic)
print(np_arr_auto.dtype)
print(type(np_arr_auto)) """

arr =np.arange(0,11*12).reshape((11,12))
print(np.unravel_index(99,(11,12)))

a = np.array([6,7,5,8])
b = np.array([4,3,7,8])

c=a.dot(b)
print(c)

print(np.sort(a)[::-1])

d = np.array([1,2,3,5,4,6,7,8,5,3,2])
print(d[2:-3])

print("Odd: ",d[1::2])

e1 =np.array([1,2,3,4])
e2 =np.array([5,6,7,8])

print("Merging:\n", np.stack((e1,e2),axis=1))

f1 = np.array([[1,2],[3,4]])
f2 = np.array([[5,6]])

print("T function with concat\n",np.concatenate((f1,f2.T),axis=1))

g1 = np.array([[1,2,3,4,5],[20,30,40,50,60]])
g2 = np.array([[6,7,8,9,10],[9,8,7,6,5]])
g3=np.column_stack([g1,g2])
print("Coulm Stack\n",g3)


h1 = np.array([1,3,16,2,4,38,9,10,12,7])
print("Greater than 5\n",h1[h1>5])

i1 = np.array([1,3,6,2,4,8,9,10,12,21])
print(i1 % 3)
print("Divisible by 3\n",i1[i1 % 3 ==0])

j1 = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80]
print(j1[j1 % 2])
