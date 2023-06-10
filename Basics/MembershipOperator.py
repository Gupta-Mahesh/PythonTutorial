
#use of In and not in

str="maheshkumargupta"
print("he" and "ta" in str)
print("hea" and "aa" not in str)

print()
lst=[1,2,3,4,5]
print(1 in lst)         #CHECK ONLY ELEMENT
print([1,2] in lst)     #FALSE BCOZ GROUP OF ELEMENT(LIST)
print(1 and 2 in lst)
print(3 not in lst)
print(6 in lst)

print()
dct={10:"hello",20:"world",30:"Namste"}
print("In:",10 in dct)            #CHECK ONLY KEY ELEMENTS
print("NOT IN:",40 not in dct)
