
'''
# Dictionary in Python is a collection of keys values, used to store data values like a map, which, 
# unlike other data types which hold only a single value as an element.
'''

#empty dict

a_dict={}
print(a_dict)
print(type(a_dict))

print("\n")
b_dict={101:"Mahesh", 102:"Kumar", 103:"Gupta", 104:"Software"}
print("Printing dict:\n",b_dict)

# another way to create dict
print("\nAnother way ")
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

print("\n")
print("Adding element: ")
b_dict[105]="Engineer"
print(b_dict)

print("\n")
print("Nested element Adding: ")
b_dict[106]={"Nested":{108:"Hridyansh", 109:"Ritvika", 110:"Hello"}}
print(b_dict)

print("\nAccessing nested item:", b_dict[106]["Nested"][108])


print("All dictionary methods\n")

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
  
# copy() method # copying dict1 data to dict2
dict2 = dict1.copy()
print("\nDict1 copied to dict1: ",dict2)
  
# clear() method
dict1.clear()
print("Clear the dict1 ",dict1)
  
# get() method
print("Get method for 1 ",dict2.get(1))
  
# items() method
print("Items method: ",dict2.items())
  
# keys() method
print("Keys: ",dict2.keys())
  
# pop() method
dict2.pop(4)
print("pop method",dict2)
  
# popitem() method
dict2.popitem()
print("Popitem: ",dict2)
  
# update() method
dict2.update({3: "Scala"})
print("Update the 3: ",dict2)
  
# values() method
print("Values: ",dict2.values())


print("\n\n")
dict_ex={1:"abc",2:"def",3:"ghi"}
lst=[1,2,3]
for i in lst:
    print(dict_ex.get(i))