class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass



class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print("r area")