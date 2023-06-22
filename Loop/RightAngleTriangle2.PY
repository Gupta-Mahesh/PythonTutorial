
s=int(input("Enter the num "))

for row in range(1,s+1):
        for column in range(1,s+1):
            if row==column or row==s:
                  print("*", end=" ")
            elif column==1:
                  print("*", end=" ")
            else:
                print(" ",end=" ")
        print()