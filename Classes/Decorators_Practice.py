
#Decorator function

def functionDecorator(func):
    def innerFunc():
        print("Inner function")
        func()
    return innerFunc

def printEx():
    print("Function without decorator") 

@functionDecorator
def printEx1():
    print("Function with decorator")

printEx()
print("\n")
printEx1()

#Another example of decorator

print("Another example of decorator\n")

#basic function

def deco_sub(funcu):    
    def checksmallervalue(a,b):
        if a<b:
            a,b = b,a
        funcu(a,b)
    return checksmallervalue

#here may be some time value print in minus if a < b, so we tring to handle this cases using decoroator
@deco_sub
def sub(a,b):
    print(a-b)

print("The sum of value is: ",end=" ")
sub(110,511)
