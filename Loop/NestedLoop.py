
#printing 2 list by using nested loop

list1=["I am", "You are", "They are"]
list2=["healthy", "naughty", "happy person", "baklol also"]

for i in list1:

    j=0
    while j<len(list2):
        print(i, list2[j],)
        j+=1
    print()
print("Bye bye")