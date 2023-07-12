
#Example 1 public access

class Car:

    def __init__(self) -> None:
        self.model="Auto Drive"
        self._fuel="Petrol"             #Sinle underscore | Suggest that Don't use this variable, it might be change | like private
        self.__color="White"            #Double underscore | It is not acceesable outside the class directly | but can be used |private variable

car=Car()

#accessing the variables
print(car.model)

#accessing the suggested to avoid var
print(car._fuel)

#accessing the private member
#print(car.__color)                  #It will throw error
                    # But it can be acceessible using --> print(car._Car__color)

#getattr() – This function is used to access the attribute of object.

attr=getattr(car,"model")
print("Check model by getattr(): ",attr)

#attr1=getattr(car,"models")    It will throw error as no attributr present
#print(attr1)

#hasattr() – This function is used to check if an attribute exist or not.

print(hasattr(car,"model"))
print(hasattr(car,"models"))

#check attribite available or not

if hasattr(car,"model"):
    print("Has model attribute")
else:
    print("Not has model attribute")

#setattr() – This function is used to set an attribute. If the attribute does not exist, then it would be created.

setattr(car,"model","XUV")
setattr(car,"model_year", "2020")
print(car.model)
print(car.model_year)


#delattr() – This function is used to delete an attribute. If you are accessing the attribute after deleting it raises error “class has no attribute”.
delattr(car,"model")
print("Deleted model: ",car.model)