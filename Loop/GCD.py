
def gcd(a, b):
    
    # code here to calculate and return gcd of a and b
    while b:
        #print(a,b)
        a, b = b, a % b
        print(a, b)
    return a

print("Final output: ",gcd(15,20))

