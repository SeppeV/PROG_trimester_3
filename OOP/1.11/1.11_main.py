# This file should be used to show the implementation of finance.py 
# For instructions read the README.md
from curses.textpad import rectangle
from shapes import *

rectangle = Rectangle(22, 5)
square = Square(8)

print(rectangle)
print(rectangle.get_perimeter())
print(rectangle.get_area())
print(rectangle.get_diagonal())

print(square)
print(square.get_perimeter())
print(square.get_area())
print(square.get_diagonal())
