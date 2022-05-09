from turtle import Shapes

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        peri = 2 * self.width + 2 * self.height
        return peri

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_diagonal(self):
        dia = (self.width**2 + self.height**2) ** 0.5
        return dia
    
class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)
        
    def __repr__(self):
        string = f"Square(side={self.width})"
        return string

    def set_side(self, side):
        self.width = side
        self.height = side

    
    

    