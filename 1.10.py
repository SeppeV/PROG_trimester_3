from cmath import pi
from turtle import Shape

class Shape:

    def __init__(self, x_coördinaat, y_coördinaat):
        self.x_coördinaat = x_coördinaat
        self.y_coördinaat = y_coördinaat

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    
    def area(self):
        a = (self.r**2) * pi
        return a

    def perimeter(self):
        r = 2 * pi * self.straal
        return r
    
    def __init__(self, r,x_coördinaat, y_coördinaat):
        super().__init__(x_coördinaat, y_coördinaat)
        self.r = r

class Rectangle:

    def __init__(self, width, height, x_coördinaat, y_coördinaat):

        Shape.__init__(self, x_coördinaat, y_coördinaat)
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        a = self.width * self.height
        return a

    def perimeter(self):
        b = (self.width + self.height) * 2
        return b

class Square(Rectangle):

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
