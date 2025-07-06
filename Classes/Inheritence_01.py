#Parent Class
class College:
    classes="MCA"
    hostel="Boys hostel"
    lab="Computer Lab"

    def __init__(self) -> None:
        print("Classes\t:",self.classes)
        print("Hostel\t:", self.hostel)
        print("Labs\t:",self.lab)

    def showDetails(self):
        print("Classes\t:","MBA")
        print("Hostel\t:", "Food court")
        print("Labs\t:", "Engineering lab")
    
    def showBCADetails(self):
        print("Classes\t:","BCA")
        print("Hostel\t:", "Avaialble")
        print("Labs\t:", "Computer lab")


"""Single inheritance
    child class
    """

class Principal(College):
    def __init__(self) -> None:
        print("\nCalled super class value by using super method.")
        super().__init__()
    
    def showDetails(self):
        print("Management\t:","MBA | MCA")
        print("Hostel report\t:", "Vardon take care")
        print("Labs\t:", "Verified all labs")

#parent class
print("\nParent class called")
principle=Principal()

#child class
princialInstance=Principal()

print("\nFirst verified in child class if method exist printed the details of child class else the parent class method's values will print")
princialInstance.showDetails()

print("\nCalled the super class method by using child class instance")
princialInstance.showBCADetails()

