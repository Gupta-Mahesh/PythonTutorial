#In this program, user will enter infine number and it will count of them.

number=int(input("Enter the nth value: " ))
print(number)
lst =[]
sum =0
for i in range (0,number):
    if i<=number:
        print("Enter the number of {}".format(i))
        lst.append(int(input()))
        sum+=lst[i]

print("List value is:",lst)

print(sum)