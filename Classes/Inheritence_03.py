
class Univerisity:
    courses="BCA","MCA","BBA","MBA"
    games="Cricket"
    teachers=10

    def __init__(self) -> None:
        print("Calling the :", Univerisity.__name__, "Class")
        print("Supported courses\t: ",Univerisity.courses,"\t" ,type(Univerisity.courses))
        print("Games\t:", Univerisity.games)
        print("No of teachers\t:", Univerisity.teachers)

class CollegeA():
    courses="BCA","MCA"
    games="Cricket"
    teachers=10
    def __init__(self) -> None:
        print("Calling the :", CollegeA.__name__, "Class")
        print("Supported courses\t: ",CollegeA.courses,"\t")
        print("Games\t:", CollegeA.games)
        print("No of teachers\t:", CollegeA.teachers)

class HOD(Univerisity, CollegeA):
    def __init__(self):
        super().__init__()

    def course(self,degree):
        print("\nCalling the course() function")
        if degree=="BCA":
            print("It is Information technology")
        elif degree=="BBA":
            print("It is business related")
        else:
            print("This degree is under progress")

hod=HOD()
hod.course("BCA")
print()
