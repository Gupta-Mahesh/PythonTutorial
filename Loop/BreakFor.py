
#Break is use for to break a loop statement

for i in range(0, 10+1):
    if i==5:            #once condition get true, here break will execute
        break
print(i)



#Smallest divisor 

num =int(input("Enter the number: "))
for i in range(2, num+1):
    if num%i ==0:
        break
print("This number is divisible by",i)

words="i am not india"
char=0
while True:
    print(words[char], end=" ")
    if words[char]=="t":
        break
    char+=1
