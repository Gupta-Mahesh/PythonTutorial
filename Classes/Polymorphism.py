
"""Method level polymorphism"""

#first method
def sum(a,b,c=0):
    return a+b+c

#sec method             this is called function overloading, where always last declaired function will be called
""" def sum(a,b,c=0):
    return a+b """

print(sum(1,2,3))       #calling the method with different literals

print(sum(1,2))
