print ("hello")


class Dog:
    pass


srt="ABC"
output =[]
for i in range(0,len(srt)):
    for j in range(len(srt), i, -1):
        print(srt[j-1],end="")
    print(output)