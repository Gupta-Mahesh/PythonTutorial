
#Continue statement
#in this program if value is divisble by 3 then that value will not print and program will continue 
i=list(range(1,11))
print(i)

for x in i:
    if x%3==0:
        continue
    print(x)

print("\n\n")

#guess the output
print("bhkkkkkkk")
num_list=[10,22,13,14,5,55,85,44,33,7,89]
y=0
while y < len(num_list):
    #print(num_list[y])
    if num_list[y]%5==0:
        y+=1
        continue

    if num_list[y]%7==0:
        y+=1
        continue

    print(num_list[y])
    y+=1
