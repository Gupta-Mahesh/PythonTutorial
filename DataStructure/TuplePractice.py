
#creating a tuple

tuple_value=(1,12,"MH","UP" )
print(tuple_value)
print(type(tuple_value))

#another way to create tuple
tuple_without_paranth=1,12,"TS", "TN","AP",12.50
print(tuple_without_paranth)
print(type(tuple_without_paranth))

#accessing the data

print(tuple_value[1])
print(tuple_without_paranth[1:])
print(tuple_without_paranth[-1])

print(tuple_without_paranth.count("abc"))
print(tuple_without_paranth.index(12))          #Find the index by value

