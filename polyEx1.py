#program for displaying polymorphism
class circle:
    def area(self,r):
        self.ac=3.14*r**2
        print("Area of circle=",self.ac)
class square(circle):
    def area(self,s):
        self.sa=s**2
        print("Area of Square=",self.sa)
        print("-"*40)
        super().area(1.4)
class Rect(square):
    def area(self,l,b):
        self.ar=l*b  
        print("Area of Rect=",self.ar)
        print("-"*50)
        super().area(4)
#main program
r=Rect()
r.area(10,20)