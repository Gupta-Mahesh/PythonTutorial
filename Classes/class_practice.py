
# Empty class
class Empty:
    pass

class Animal:
    animal_type="NA"
    animal_age=0
    pet_status="NO"

    def __init__(self, animal_type, animal_age, pet_status): 
        self.animal_type=animal_type
        self.animal_age=animal_age
        self.pet_status=pet_status
        print("Animal Type: ",self.animal_type)
        print("Animal Age: ",self.animal_age)
        print("Animal Pet or Not: ",self.pet_status)

    def printAnimal(self):
        print("Animal Type: ",self.animal_type)
        print("Animal Age: ",self.animal_age)
        print("Animal Pet or Not: ",self.pet_status)

animal=Animal("Dog",1,"Yes")
print(animal.printAnimal())
#animal=Animal("cat",2,"Yes")
print(Animal("cat",2,"Yes").animal_age)