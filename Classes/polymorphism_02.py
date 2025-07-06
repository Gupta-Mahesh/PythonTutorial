
"""Class level overloading"""
class Father:
    def __init__(self,name,addr) -> None:
        self.nam =name
        self.addr =addr
    def name(self):
        return self.nam
    
    def address(self):
        return self.addr 
     
class Son:
    def __init__(self,name,addr) -> None:
        self.nam =name
        self.addr =addr
    def name(self):
        return self.nam
    
    def address(self):
        return self.addr 
    
obj_father=Father("Rajendra","Jnp")
obj_son=Son("Mahesh", "Hyd")

for obj in (obj_father, obj_son):
    print("Name \t:", obj.name())
    print("Address\t:", obj.address())
