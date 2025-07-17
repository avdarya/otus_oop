from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        super().validate_side(side_a)
        super().__init__(side_a, side_a)
