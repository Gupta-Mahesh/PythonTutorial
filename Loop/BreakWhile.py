#find the char and break if statement true
print("\n\nFind the available character")
words="i am not india"
char=0
while True:
    print(words[char], end=" ")
    if words[char]=="t":
        break
    char+=1



print("\n\nFind the Smallest Division number")
#Smallest divisor 
try:
    num = int(input("Enter the number: "))
except ValueError:
    num = 0

i = 2
while num>0 & i<num:
    if num%i ==0:
        break
    i+=1
print("This number is divisible by",i)

"""
for i in range(2, num+1):
    if num%i ==0:
        break
print("This number is divisible by",i)
"""
