import pytest


@pytest.mark.parametrize(
    'figure_type_1, sides_1, figure_type_2, sides_2',
    [
        ('rectangle', (10, 20), 'rectangle', (3, 2.1)),
        ('rectangle', (10.3, 20), 'square', (5,)),
        ('rectangle', (10, 20), 'triangle', (3, 4, 5)),
        ('rectangle', (10, 20), 'circle', (7,)),
        ('square', (5,), 'square', (6,)),
        ('square', (5,), 'triangle', (3, 4, 5)),
        ('square', (5,), 'circle', (7,)),
        ('triangle', (3, 4, 5), 'triangle', (3.2, 4.3, 5.6)),
        ('triangle', (3, 4, 5), 'circle', (7,)),
        ('circle', (7,), 'circle', (2.1,))
    ]
)
def test_figure_add_area(get_figure, figure_type_1, sides_1, figure_type_2, sides_2):
    figure_1 = get_figure(figure_type_1, *sides_1)
    figure_2 = get_figure(figure_type_2, *sides_2)

    assert figure_1.area + figure_2.area == figure_1.add_area(figure_2)
    assert figure_1.area + figure_2.area  == figure_2.add_area(figure_1)

@pytest.mark.parametrize(
    'figure_type, sides, invalid_type',
    [
        ('rectangle', (10, 20), 'abc'),
        ('rectangle', (10.3, 20), 1),
        ('rectangle', (10.3, 20), 2.3),
        ('rectangle', (10, 20), None),
        ('rectangle', (10, 20), True),
        ('square', (5,), 'abc'),
        ('square', (5,), 1),
        ('square', (5,), 2.3),
        ('square', (5,), None),
        ('square', (5,), True),
        ('triangle', (3, 4, 5), 'abc'),
        ('triangle', (3, 4, 5), 1),
        ('triangle', (3, 4, 5), 3.4),
        ('triangle', (3, 4, 5), None),
        ('triangle', (3, 4, 5), True),
        ('circle', (7,), 'abc'),
        ('circle', (7,), 1),
        ('circle', (7,), 5.3),
        ('circle', (7,), None),
        ('circle', (7,), True)
    ]
)
def test_figure_invalid_adding(get_figure, figure_type, sides, invalid_type):
    figure = get_figure(figure_type, *sides)
    with pytest.raises(ValueError):
        figure.add_area(invalid_type)