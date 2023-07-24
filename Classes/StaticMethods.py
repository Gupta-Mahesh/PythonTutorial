
"""Static method"""

class StaticMethodClass:

    name = "Kumar"              #Class variable | Static variable

    @staticmethod
    def infoPrint():
        print("This is a static method")
        print("class variable ",StaticMethodClass.name)
        StaticMethodClass.name +=" Gupta"
        print("class variable ",StaticMethodClass.name)

StaticMethodClass.infoPrint()                       #static method not required to create object to call static method


