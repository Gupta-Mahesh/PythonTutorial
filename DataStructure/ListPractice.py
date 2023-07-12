
#create and print list

# Creating a empty List
emptyList = []
print("Blank List: ",emptyList)

emptyList1 = list()
print("Blank List using list function: ",emptyList1)

test=list([1,2,2])
print(type(test))
print(test)


Var = ["Create", "a", "List"]
print(Var)

var2=["Mahesh", 9598494948, "Hyderabad", 8.5]
print(var2)

print(var2[0])          #It will print 0 index's value
print(var2[1:])         #first element (0 index) wont print here


###############################################
# Multi-dimensional list

List = [['Geeks', 'For'], ['Geeks']]
print("Accessing a element from a Multi-Dimensional list")
print(List[0])              # First list
print(List[1])              # Sec list

print(List[0][0],List[0][1])    


print("\n\n")
#Negative index

number = [1, 2, 'three', 4, 'five', 6, 'seven']
print(number[-1])
print(number[-4])

# Adding element in list
print("\n\n")

add_elem_list=[]
print("Print empty element ",add_elem_list)
add_elem_list.append(0)
add_elem_list.append("Mahesh")
add_elem_list.append(10.5)

print("Printing after adding element ",add_elem_list)

# Using insert() method

add_elem_list.insert(2,"Software")
print(add_elem_list)

#count method
list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']
print(list2.count('a'))


#del keyword        It is deleting by index

numbers_del = [1, 2, 3, 2, 3, 4, 5]
del numbers_del[2]
print(numbers_del)


#remove() method it is deleting by first matching value
numbers_rem = [1, 2, 3, 2, 3, 4, 5]
numbers_rem.remove(3)
print(numbers_rem)

#pop() method   It is deleting by index and also will show the deleted value
numbers_pop = [1, 2, 3, 2, 3, 4, 5]
numbers_pop.pop(3)
print(numbers_pop)


#max() method
print("Max value: ",max(4,12,43.3,19,100))
numbers_max=[22,55,4,8899,77,77,55,77]
print("Max value: ",max(numbers_max))

#It will throw error as only one type data required to check max
#numbers_alpha_max=[1,2,4,5,2,"a","c",55]
#print(max(numbers_alpha_max))           

#min() method
print("Min value: ",min(numbers_max))

#sort() function
print(numbers_max,"Sort: ", end=" ")
numbers_max.sort()
print(numbers_max)

numbers_max.reverse()
print("Reverse: ",numbers_max)

print(len(numbers_max))


list_val=[0.5*x for x in range(0,4)]
print(list_val)

