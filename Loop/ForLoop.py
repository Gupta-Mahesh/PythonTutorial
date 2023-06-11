
#WithVariable 2 ka table
print("List using range function")
for i in range(2,21,2): print(i, end=" ")
print()

#String
print("\nString")
text="Tera Bap Chor Hai"
for i in text:
    print(i, end="~")

#List
print("\nList")
list_num =list(range(1,11))
print(list_num)
for i in list_num:
    print(i, end=" ")

print()

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("",i, d[i])

print("\nDict self created")
dictionary={"Name":"Mahesh","Father":"Rajendra", "Add":"Hyderabad"}
for i in dictionary:
    print(i,": ",dictionary[i]) 