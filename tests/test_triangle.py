import pytest
from src.triangle import Triangle

@pytest.mark.parametrize(
    'side_a, side_b, side_c, area',
    [
        (3, 4, 5, 6),
        (3.2, 4.3, 5.6, 6.84),
        (6, 7.4, 8, 21.16)
    ],
    ids=['integer', 'float', 'integer + float']
)
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == pytest.approx(area,  abs=0.01), f'Expected area={area}, got {t.area}'

@pytest.mark.parametrize(
    'side_a, side_b, side_c, perimeter',
    [
        (3, 4, 5, 12),
        (3.2, 4.3, 5.6, 13.1),
        (6, 7.4, 8, 21.4)
    ],
    ids=['integer', 'float', 'integer + float']
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == pytest.approx(perimeter,  abs=0.01), f'Expected perimeter={perimeter}, got {t.perimeter}'

@pytest.mark.parametrize(
    'side_a, side_b, side_c',
    [
        (4, 5, 10), (5, 5, 10),
        (29, 7, 12), (29, 7, 22),
        (5, 16, 10), (8, 16, 8)
    ]
)
def test_is_exist_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize(
    'side_a, side_b, side_c',
    [
        (0, 4, 5), (3, 0, 5), (3, 4, 0),
        (-1, 4, 5), (3, -1, 5), (3, 4, -1)
    ],
    ids=[
        'side_a=0', 'side_b=0', 'side_c=0',
        'side_a<0', 'side_b<0', 'side_c<0'
    ]
)
def test_triangle_nonpositive_side(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize(
    'side_a, side_b, side_c',
    [
        ("a", 4, 5), (3, "b", 5), (3, 4, "c"),
        (None, 4, 5), (3, None, 5), (3, 4, None)
    ],
    ids=[
        'side_a is str', 'side_b is str', 'side_c is str',
        'side_a is None', 'side_b is None', 'side_c is None'
    ]
)
def test_triangle_invalid_side(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        Triangle(side_a, side_b, side_c)
