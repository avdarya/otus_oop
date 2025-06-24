from math import sqrt

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().validate_side(side_a, side_b, side_c)
        if (
            side_a + side_b <= side_c or
            side_b + side_c <= side_a or
            side_a + side_c <= side_b
        ):
            raise ValueError(f"Triangle does not exist. Got sides: {side_a}, {side_b}, {side_c}")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        semi_p = self.perimeter / 2
        return sqrt(semi_p * (semi_p - self.side_a) * (semi_p - self.side_b) * (semi_p - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
