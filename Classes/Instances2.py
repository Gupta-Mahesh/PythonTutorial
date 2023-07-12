
# Var() and Dir()

class VarDir:

    def __init__(self) -> None:
        self.name="Mahesh"
        self.mobile="9598494948"
    
    """ def show(self):
        print(self.name)
        print(self.mobile) """

vardir= VarDir()

print("Object print: ",vardir,"\n")
print("Dict Form: ",vars(vardir),"\n")

print("Dir form: ",dir(vardir))