
s1="youraregreat"

#revers print
print(s1[-1])   #print lasr value
print(s1[::-1]) #print revers value
print(s1[:-1])  #print print from start upto before last text

#Slicing the words
print(s1[3:6])  #print 3rd to 5th word


# ord() function
# inbuilt function return an
# integer representing the Unicode code
value = ord("A") 
# writing in ' ' gives the same result
value1 = ord('A')
# prints the unicode value
print (value, value1)


#chr() function convert asci value to alphabet

print(chr(97))


#String Concatenation using + Operator

# Defining strings
var1 = "Hello "
var2 = "World"
 
# + Operator is used to combine strings
var3 = var1 + var2
print(var3)



# index() method 
# Python String index() Method allows a user to find the index of the first occurrence of an existing substring inside a given string.

a1="This is a test"
a2="a"

print(a1.index(a2))
print(a1.index("test"))
print(a1.index("hello"))    #as the text is not present in string so it will throw exception


