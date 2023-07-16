
#Default argument use
#Suppose use do not have info of any of the field, then by default some value will take
#Here address give as Default as NA

def printArguments(name, age, add="NA"):
    print("Name: "+name,"\nAge: ",age,"\nAddress: "+add)

printArguments("Mahesh", 35, "Balkampet")
print("\n\n")
printArguments("Allu Arjun", 40,)   # the default value will be print as NA