#sample program for constructor over-riding.
class Circle:                           #original constructor
    def __init__(self):
        print("Drawing Circle")
class Rect(Circle):                     #overridden constructor
    def __init__(self):
        print("Drawing Rectangle")
class Square(Rect):                    #overridden constructor
    def __init__(self):
        print("DraWING sQUARE")
        Rect.__init__(self)
        Circle.__init__(self)
      
#Main program
S=Square()