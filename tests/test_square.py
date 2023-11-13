import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(2, 4), (5, 25), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(2, 8), (3, 12), (22, 88)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
