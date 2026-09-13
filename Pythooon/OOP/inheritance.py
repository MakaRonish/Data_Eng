class Animal:
    def __init__(self,name):
        self.name=name
        self.eye=2


    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Sparrow(Animal):

    def __init__(self,city):
        super().__init__("sparrow")
        self.city= city


    def fly():
        print("flying")


s1= Sparrow("tx")
print(s1.name)





        