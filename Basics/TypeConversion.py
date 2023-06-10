#Type conversion -> Implicit and explicit 

sample = open('file.txt', 'w')

print("#Implicit",file=sample)
num_int=10
num_float=10.1
sum=num_int+num_float

print(sum)

d = True
e = num_int + d  # bool convert to 1 or 0
print(e)

print()
print("#Explicit conversion")
s = '135'
i = 10 + int(s)  # str to int conversion
f = float(s)  # str to float conversion

print(i)
print(f)

print()
#Conversion string to list, tuple and set
print("#Conversion string to list, tuple and set")
s = 'geeks'
print("String:",s)
print('String to list', list(s))
print('String to tuple', tuple(s))
print('String to set', set(s))

print()
#Conversion tuple to list and set to list
t = (10, 20, 30)
print('tuple to list', list(t))
s = {10, 20, 30}
print('set to list', list(s))

print()
print("Int to bunary, hex and oct")
# int to binary, hex and oct
a = 20
print('int to binary 20-->', bin(a))
print('int to hexa 20-->', hex(a))
print('int to octa 20-->', oct(a))

print()
# binary to int, oct and hex
print("Binary to int, oct and hex")
a = "1001"
print('binary to int', int(a, 2))  # base is 2
b = "12"
print('oct to int', int(b, 8))  # base is 8
c = "A1"
print('hexa to int', int(c, 16))    # base is 16
