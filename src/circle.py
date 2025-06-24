import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().validate_side(radius)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
