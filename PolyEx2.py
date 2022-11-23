#program for displaying polymorphism
class circle:
    def area(self,r):
        self.ac=3.14*r**2
        print("Area of circle=",self.ac)
        #super().area(float(input("Enter radius:")))...AttributeError: 'super' object has no attribute 'area'
class square(circle):
    def area(self,s):
        self.sa=s**2
        print("Area of Square=",self.sa)
        print("-"*40)
        super().area(float(input("Enter radius:")))
class Rect(square):
    def area(self,l,b):
        self.ar=l*b  
        print("Area of Rect=",self.ar)
        print("-"*50)
        super().area(float(input("Enter side:")))
#main program
r=Rect()
r.area(float(input("Enter length:")),float(input("Enter breadth:")))