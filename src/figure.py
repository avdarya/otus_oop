from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self) -> int:
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"Expected Figure, got {figure.__class__.__name__}")
        return self.area + figure.area

    @staticmethod
    def validate_side(*sides):
        for side in sides:
            if not isinstance(side, int | float):
                raise TypeError(f"Expected int or float. Got {type(side).__name__}")
            if side <= 0:
                raise ValueError(f"Side must be > 0. Got side={side}, sides={sides}")
