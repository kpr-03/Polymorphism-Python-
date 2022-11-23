#PolyEx4.py
class Circle:
	def  area(self,r):  # Original Method
		self.ac=3.14*r**2
		print("Area of Circle=",self.ac)

class Square:
	def area(self,s):#Original Method
		self.sa=s**2
		print("Area of Square=",self.sa)
		print("-"*40)

class Rect(Circle,Square):
	def area(self,l,b):  # Overridden Method
		self.ar=l*b
		print("Area  of Rect:",self.ar)
		print("-"*50)
		super().area(float(input("Enter Radius:")))
		print("-"*50)
		Square.area(self, float(input("Enter Side:")))

#main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")))