
s=int(input("enter the num "))

for i in range(s):
        for j in range(s):
            if i==0 or j==0  :
                print("*", end=" ")  
            elif  i==s-1 or j==s-1 :
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()