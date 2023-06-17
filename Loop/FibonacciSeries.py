
num=int(input("Number "))

# 1 1 2 3 5 8 13 

count=2
prev=1
curr=1
temp=0
print(prev, curr, end=" ")
#print(curr)
while True:
    if(num==1 or num==2):
        print(num)
    elif(num>2):
        count +=1
        temp=prev+curr
        prev=curr
        curr = temp
        print(curr,end=" ")
        if count==num:
            print("\n\n",count)
            break