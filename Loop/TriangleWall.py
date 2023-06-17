
s=int(input("Enter the num "))

for i in range(1,s+1):
        for y in range(i):
            print("*",end=" ")
        print()


for i in range(1,s+1):
        for y in range(s+1,i, -1):
            print("*",end=" ")
        print()

print()
for i in range(s):
        for j in range(s, i, -1):
            print("*", end=" ")
        print()

ans=0
for num in range(1,s+1):
        ans +=num
print(ans)

print()
for i in range(1, s+1):
        if s%i==0 :
            print(i, end = ' ')
            continue


print("\n\n")
for i in range(s):
        if i == 0 :
            print("*")
        elif i < (s-1):
            
            print("*","  "*(i-1),"*")
        else:
            print("* "*s)