import pytest
from src.square import Square

@pytest.mark.parametrize(
    'side_a, area',
    [
        (3, 9),
        (4.2, 17.64)
    ],
    ids=['integer', 'float']
)
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == pytest.approx(area,  abs=0.01), f'Expected area={area}, got {s.area}'

@pytest.mark.parametrize(
    'side_a, perimeter',
    [
        (3, 12),
        (4.2, 16.8)
    ],
    ids=['integer', 'float']
)
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == pytest.approx(perimeter,  abs=0.01), f'Expected perimeter={perimeter}, got {s.perimeter}'

@pytest.mark.parametrize(
    'side_a', [0, -1], ids=['side_a=0', 'side_a<0']
)
def test_square_nonpositive_side(side_a):
    with pytest.raises(ValueError):
        Square(side_a)

@pytest.mark.parametrize(
    'side_a', ["a", None], ids=['side_a is str', 'side_a is None']
)
def test_square_invalid_side(side_a):
    with pytest.raises(TypeError):
        Square(side_a)
