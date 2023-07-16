
#in this file going to create object of the class

class Base:
    
    #class level attribute
    name="NA"

    @classmethod
    def welcomeWishToAll(self, wish="Hi!"):
        print(f"{wish} Everyone ")              #here the after printing this statement, function return None so none will print in output
                                                #If we use print fucnction while calling should avoid print again (two print f() will return none)
    def byeToAll(self, wish):
        return f"{wish} to All "
    

b1=Base()
print(b1)
print(type(b1))

#calling the attributes using class without instances
print(Base.name)
Base.name="Mahesh Kumar"
print(Base.name)
print(Base.byeToAll("","Good"))

#creating instance and calling the attribute
print("\n")
b2=Base()
print(b2.name)
b2.name="Gupta"
print(b2.name)
b2.welcomeWishToAll()
b2.welcomeWishToAll("Good morning!")

print(b2.byeToAll("Namaste!"))
b2.address="Hyderabad"                  #in python we can add attribute after creating object which is not possible in other languages
print("Address: ",b2.address)                       #Here address attribute was not present in class but here we have added

