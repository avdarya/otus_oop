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
            raise ValueError(f"Argument figure must be type of Figure. Got {figure.__class__}")
        return self.area + figure.area

    @staticmethod
    def validate_side(*sides):
        for side in sides:
            if side <= 0:
                raise ValueError(f"Argument side must be greater than 0. Got side={side}, sides={sides}")