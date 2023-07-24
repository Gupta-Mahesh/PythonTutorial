
class Univerisity:
    courses="BCA","MCA","BBA","MBA"
    games="Cricket"
    teachers=10

    def __init__(self) -> None:
        print("Supported courses\t: ",Univerisity.courses,"\t" ,type(Univerisity.courses))
        print("Games\t:", Univerisity.games)
        print("No of teachers\t:", Univerisity.teachers)

class CollegeA():
    courses="BCA","MCA"
    games="Cricket"
    teachers=10
    def __init__(self) -> None:
        print("College A: ")
        print("Supported courses\t: ",CollegeA.courses,"\t")
        print("Games\t:", CollegeA.games)
        print("No of teachers\t:", CollegeA.teachers)

class CollegeB():
    courses="BCA","MCA"
    games="Cricket"
    teachers=10
    def __init__(self) -> None:
        print("College B: ")
        print("Supported courses\t: ",CollegeB.courses,"\t")
        print("Games\t:", CollegeB.games)
        print("No of teachers\t:", CollegeB.teachers)

#Multiple inheritence calling three methods in single class
class Seeker(CollegeA,CollegeB,Univerisity):
    def __init__(self) -> None:
        print("Seeker is looking for the courses")
        super().__init__()

seek=Seeker()       #If method name same in both parent classes, it will call the method of first class


