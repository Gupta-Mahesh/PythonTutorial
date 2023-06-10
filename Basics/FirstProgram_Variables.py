#For single line use hash operator, pythoin program will treat as comment

"""
This is multiline comment
where we can write a paragraph
"""
print("First line of program")

# Variable String and numbers
print("\n\nCreating a variable")

num=55
strs="This is a string variable"
print("Printing the variables")
print("Declared String : "+strs)
print("Declared Number :{}".format(num))

#Casting
#If you want to specify the data type of a variable, this can be done with casting.
print("\n\nType Casting variable")
x=int(9)
y=str("hello")
z=float(9)
z1=chr(65)

print(x)
print(y)
print(z)
print(z1)

#Get the Type
#You can get the data type of a variable with the type() function.
print("\n\nGet the Type Of Variable")
print(type(x))
print(type(y))
print(type(z))
print(type(z1))


#Single or Double Quotes both will work as String
print("\n\nUse of single and Double qoute")
x='Single qoute'
y="Double qoute"
print(x)
print(y)

#python is also Case-Sensitive
print("\n\nCase sensitive")

x="x is Small letter"
X="X is capital letter"
print(X)
print(x)

#Many Values to Multiple Variables
print("\n\nMultiple variable")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

