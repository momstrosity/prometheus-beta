import pytest
from src.even_number_doubler import double_even_numbers

def test_double_even_numbers_normal_case():
    """Test that even numbers are doubled and odd numbers remain unchanged."""
    input_list = [1, 2, 3, 4, 5, 6]
    expected_output = [1, 4, 3, 8, 5, 12]
    assert double_even_numbers(input_list) == expected_output

def test_double_even_numbers_empty_list():
    """Test that an empty list returns an empty list."""
    assert double_even_numbers([]) == []

def test_double_even_numbers_all_odd():
    """Test that a list of all odd numbers remains unchanged."""
    input_list = [1, 3, 5, 7, 9]
    assert double_even_numbers(input_list) == input_list

def test_double_even_numbers_all_even():
    """Test that a list of all even numbers is doubled."""
    input_list = [2, 4, 6, 8]
    expected_output = [4, 8, 12, 16]
    assert double_even_numbers(input_list) == expected_output

def test_double_even_numbers_zero():
    """Test that zero (an even number) is doubled."""
    assert double_even_numbers([0]) == [0]

def test_double_even_numbers_negative_numbers():
    """Test that negative even and odd numbers are handled correctly."""
    input_list = [-1, -2, -3, -4]
    expected_output = [-1, -4, -3, -8]
    assert double_even_numbers(input_list) == expected_output

def test_double_even_numbers_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        double_even_numbers("not a list")

def test_double_even_numbers_invalid_element_type():
    """Test that a TypeError is raised for lists with non-numeric elements."""
    with pytest.raises(TypeError, match="All elements in the list must be numeric"):
        double_even_numbers([1, 2, "three", 4])