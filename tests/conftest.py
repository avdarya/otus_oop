import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture()
def get_figure():

    def _wrapper(figure_type: str, *sides):
        if figure_type == 'rectangle':
            return Rectangle(*sides)
        if figure_type == 'square':
            return Square(*sides)
        if figure_type == 'triangle':
            return Triangle(*sides)
        if figure_type == 'circle':
            return Circle(*sides)

        raise ValueError(f'Invalid figure_type, got {figure_type}')

    yield _wrapper
