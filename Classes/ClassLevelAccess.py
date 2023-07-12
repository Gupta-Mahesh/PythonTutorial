
#Example 1 public access

class Car:

    def __init__(self) -> None:
        self.model="Auto Drive"
        self._fuel="Petrol"             #Sinle underscore | Suggest that Don't use this variable, it might be change | like private
        self.__color="White"            #Double underscore | It is not acceesable outside the class directly | but can be used |private variable



