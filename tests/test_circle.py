import pytest
from src.circle import Circle

@pytest.mark.parametrize(
    'radius, area',
    [(4, 50.27), (4.2, 55.42)],
    ids=['integer', 'float'])
def test_circle_area_positive(radius, area):
    c = Circle(radius)
    assert c.area == pytest.approx(area,  abs=0.01), f'Expected area={area}, got {c.area}'

@pytest.mark.parametrize(
    'radius, perimeter',
    [(4, 25.13), (4.2, 26.39)],
    ids=['integer', 'float']
)
def test_circle_perimeter_positive(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == pytest.approx(perimeter,  abs=0.01), f'Expected perimeter={perimeter}, got {c.perimeter}'

@pytest.mark.parametrize(
    'radius', [0, -1], ids=['radius=0', 'radius<0']
)
def test_circle_nonpositive_side(radius):
    with pytest.raises(ValueError):
        Circle(radius)

@pytest.mark.parametrize(
    'radius', ["a",  None], ids=['radius is str',  'radius is None']
)
def test_circle_invalid_side(radius):
    with pytest.raises(TypeError):
        Circle(radius)
