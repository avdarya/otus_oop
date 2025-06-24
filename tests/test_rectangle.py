import pytest
from src.rectangle import Rectangle

@pytest.mark.parametrize(
    'side_a, side_b, area',
    [
        (4, 5, 20),
        (4.2, 5.6, 23.52),
        (6, 7.4, 44.4)
    ],
    ids=['integer', 'float', 'integer + float']
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == pytest.approx(area,  abs=0.01), f'Expected area={area}, got {r.area}'

@pytest.mark.parametrize(
    'side_a, side_b, perimeter',
    [
        (4, 5, 18),
        (4.2, 5.6, 19.6),
        (6, 7.4, 26.8)
    ],
    ids=['integer', 'float', 'integer + float']
)
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == pytest.approx(perimeter,  abs=0.01), f'Expected perimeter={perimeter}, got {r.perimeter}'

@pytest.mark.parametrize(
    'side_a, side_b',
    [
        (0, 5), (4, 0),
        (-1, 3), (7, -1)
    ],
    ids=[
        'side_a=0', 'side_b=0',
        'side_a<0', 'side_b<0'
    ]
)
def test_rectangle_nonpositive_side(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)

@pytest.mark.parametrize(
    'side_a, side_b',
    [
        ("a", 2), (2, "b"),
        (None, 9), (10, None)
    ],
    ids=[
        'side_a is str', 'side_b is str',
        'side_a is None', 'side_b is None'
    ]
)
def test_rectangle_invalid_side(side_a, side_b):
    with pytest.raises(TypeError):
        Rectangle(side_a, side_b)
