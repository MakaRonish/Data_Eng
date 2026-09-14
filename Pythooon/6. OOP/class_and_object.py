class Student:
    #attribute
    # roll_no :int =0
    # name: str=""
    # age:int=0
    # standard: str=""


    #constructor
    def __init__(self, r ,n , a ,s,school="DPS"):
        self.roll_no=r
        self.name=n
        self.age=a
        self.standard=s
        self.school=school
        self.branch="non change able"



    #Methods
        
    def display(self):
        print(f"Role no = {self.roll_no}\nName = {self.name}\nAge = {self.age}\nStandard = {self.standard}\nschool = {self.school}\n Branch = {self.branch}")




s1 = Student(1,"ronish",22,"12","99")



s1.display()

    
