"""Class method"""

class ClassLevelMethod:
    
    name="Mahesh"
    empno=101
    company="Qolsys"


    @classmethod
    def change_company(cls):
        print("Print the old names", ClassLevelMethod.name, ClassLevelMethod.empno, ClassLevelMethod.company)
        ClassLevelMethod.empno="32101"
        ClassLevelMethod.company="QSI Johnson Controls"
        print("Print the new names", ClassLevelMethod.name,ClassLevelMethod.empno,ClassLevelMethod.company)

    @classmethod
    def change_info(cls,name,empno,company):
        print("Print the after merging the names", ClassLevelMethod.name, ClassLevelMethod.empno, ClassLevelMethod.company)
        ClassLevelMethod.name=name
        ClassLevelMethod.empno=empno
        ClassLevelMethod.company=company
        print("Print the emp info ", ClassLevelMethod.name,ClassLevelMethod.empno,ClassLevelMethod.company)

#calling first way
ClassLevelMethod.change_company()

claslevel=ClassLevelMethod()
claslevel.change_company()

ClassLevelMethod.change_info("Mahesh Gupta", 10101, "QSI JCI India")