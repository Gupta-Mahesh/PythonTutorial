
# Using different type of operators
"""
Operator Description Syntax
+	Addition: adds two operands	x + y
	Subtraction: subtracts two operands	x - y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when first operand is divided by the second	x % y
**	Power : Returns first raised to power second	x ** y

"""

print("### Addition ###")

a = 10
b = 20
sum= a+b
print("The sum of value is ",sum, end="\n\n")

print("### Subtraction ###")
a = 10
b = 20
sub= a-b
print("The sub value is ",sub, end="\n\n")

print("### Multiplication ###")
a = 10
b = 20
mul= a*b
print("The sub value is ",mul, end="\n\n")

print("### Division Float ###")
a = 110
b = 20
div_float= a/b
print("The Division float value is ",div_float, end="\n\n")

print("### Division Floor ###")
a = 110
b = 20
div_floor= a//b
print("The Division floor value is ",div_floor, end="\n\n")

print("### Modulus ###")
a = 110
b = 20
modul= a%b
print("The Modulus value is ",modul, end="\n\n")

print("### Power for value ###")
a = 10
b = 3
power= a**b
print("{} to power {} is".format(a,b), power, end="\n\n")

