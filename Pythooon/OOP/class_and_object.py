class Student:
    #attribute
    roll_no :int =0
    name: str=""
    age:int=0
    standard: str=""

    #Methods
    def set_information(self):
        

    def display(self):
        print(f"Role no = {self.roll_no}\nName = {self.name}\nAge = {self.age}\nStandard = {self.standard}")




s1 = Student(1,"ronish",22,"12")



s1.display()

    
