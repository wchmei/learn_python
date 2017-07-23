class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def calcutate_area(self):
        return self.width * self.heigth

    @classmethod
    def new_square(cls,side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print (square.calcutate_area())
