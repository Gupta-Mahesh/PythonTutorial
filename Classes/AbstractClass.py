"""Abstract Class
    Python dowst not provide direct access of abstract class, 
    Here It is required to import abstractmethod and ABC class"""

from abc import ABC, abstractmethod

class Manager(ABC):

    @abstractmethod
    def sanityTest(self):
        pass

    @abstractmethod
    def regressionTest(self):
        pass

class ZwaveTeam(Manager):
    
    # overriding abstract method
    def sanityTest(self):
        return "Z-Wave Sanity Testing is completed"
    
    # overriding abstract method
    def regressionTest(self):
        return "Z-Wave Regression test is in progress"

class SRFTeam(Manager):
    
    # overriding abstract method
    def sanityTest(self):
        return "SRF Sanity Testing is completed"
    
    # overriding abstract method
    def regressionTest(self):
        return "SRF regression test is 80%' completed"

class Upgrade(Manager):
    
    # overriding abstract method but not adding any logic
    def sanityTest(self):
        return super().sanityTest()

    # overriding abstract method but not adding any logic so it will return as None
    def regressionTest(self):
        return super().regressionTest()


team1=ZwaveTeam()
team2=SRFTeam()
team3=Upgrade()

for obj in (team1,team2,team3):
    print("Sanity report\t\t:\t",obj.sanityTest())
    print("Regression Report\t:\t",obj.regressionTest())

