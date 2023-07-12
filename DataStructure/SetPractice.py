
'''
Set:
Sets are unordered collections of unique items.
Set elements are enclosed in curly braces { } or created using the set() function.
Sets do not maintain any specific order of elements, and duplicate elements are automatically eliminated.
Sets support mathematical set operations such as union, intersection, and difference.
Sets are useful when you want to store a collection of distinct items and perform operations like checking membership or eliminating duplicates
'''

#creating a empty set

a_set=set()
print(a_set)

b_set={1,2,3,4,5,6,6,77,7,7}
print(b_set)                    #Duplicate value won't show

c_set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(c_set)

d_set=set()
print("d_set first: ",d_set)

d_set.add(2)
d_set.add(5)
#d_set.add(["a","b"])       #List data type cannot be added in set, bcoz of mutable
d_set.add(("c","d",2))
print(d_set)

d_set.update([2,3,7])
print(d_set)

print("\nElements of set: ")
for i in d_set:
    print(i, end=" ")


#inserting value in set
print("\n")
e_set=set()
for i in range(21):
    if i%2==0:
        e_set.add(i*2)
    else:
        e_set.add(i)
print(e_set)

if 4 in e_set:
    e_set.remove(4)
    print("After deleting 4: ",e_set)

#e_set.remove(4)        #will throw err as 4 is not present

e_set.discard(4)        #will delete if value present else ignore
e_set.discard(5)

print("deleting 5: ",e_set)


print("\n\n")

frozenset_set=frozenset([1,2,3,"A","B"])
print("Frojen Set: ", frozenset_set)
print(frozenset_set)

print("\n\n")


# Union operation on Python Sets

set1={1,2,33,55,44,"Abc","def","ghi"}
set2={21,55,77,"Abc","mbh","oiu"}

union_set=set1.union(set2)
union_set1=set1 | set2
print("Union using function: ",union_set)
print("Union using or symbol: ",union_set1)


#Intersection operation on Python Sets  //store only common item

print("\n\n")
intersection_set=set1.intersection(set2)
print("Intersection Set using Function: ",intersection_set)
intersection_set2=set1 & set2
print("Intersection Set using & operator: ",intersection_set2)


# Finding Difference of Sets in Python
print("\n\n")
different_set=set1.difference(set2)
print("Difference Set usinf function: ",different_set)

different_set2=set1-set2
print("Difference using - operator: ",different_set2 )


# Clearing Python Sets

set1.clear()
print("Clear Set: ",set1)



