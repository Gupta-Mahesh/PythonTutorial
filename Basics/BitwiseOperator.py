
#Bitwise operators
"""
In Python, bitwise operators are used to perform bitwise calculations on integers. 
The integers are first converted into binary and then operations are performed on bit by bit, 
hence the name bitwise operators. Then the result is returned in decimal format.

Note: Python bitwise operators work only on integers.
"""

a=10
b=20
print("Binary of a and b: ", bin(a), bin(b))
print("a | b ", a|b)
print("a & b ", a&b)
print("a ^ b ", a^b)
print("a ~ b ", ~a, ~b)


"""
Shift Operators
These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively. 
They can be used when we have to multiply or divide a number by two. 

Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) 
as a result. Similar effect as of dividing the number with some power of two.
"""

print("\n## Shift Operator ##\n")
c=10
d=11
print("Binary of {}: ".format(c), bin(c))
print("BInary of {}: ".format(d), bin(d))

print("Right shift {} {}: ".format(c,bin(c)), c >> 1)
print("Right Shift {} {}: ".format(d,bin(d)), d >> 2)

print("Left shift {} {}: ".format(c,bin(c)), c << 1)
print("Left Shift {} {}: ".format(d,bin(d)), d << 2)

