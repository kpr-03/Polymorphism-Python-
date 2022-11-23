class Circle:
    def draw(self):      #original method
        print("Drawing Circle")
class Rect(Circle):      #overrriden method
    def draw(self):
        print("Drawing Rectangle:")
        super().draw()
class Square(Rect):             #overrriden method
    def draw(self):
        print("Drawing Square")
        super().draw()
#main program
so=Square()
so.draw()