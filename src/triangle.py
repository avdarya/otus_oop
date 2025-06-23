from math import sqrt

from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().validate_side(side_a, side_b, side_c)
        if (
            side_a + side_b <= side_c or
            side_b + side_c <= side_a or
            side_a + side_c <= side_b
        ):
            raise ValueError(f"The sum of any two sides must be greater than the third. Got side_a={side_a}, side_b={side_b}, side_c={side_c}")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        semiperimeter = self.perimeter / 2
        return sqrt(semiperimeter * (semiperimeter - self.side_a) * (semiperimeter - self.side_b) * (semiperimeter - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c