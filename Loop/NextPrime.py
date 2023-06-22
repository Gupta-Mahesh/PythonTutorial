num = int(input("Number "))

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
def isPrime(num):
    flag = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            #print(i,"\n\n")
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True4
        if flag:
            return False
        else:
            return True



temp = num+1
while True:
    if isPrime(temp):
        print(temp)
        break
    else:
        temp+=1    