import pytest
from src.two_sum import two_sum

def test_two_sum_basic_true():
    """Test that function returns True when two numbers sum to target."""
    assert two_sum([1, 2, 3, 4], 7) == True
    assert two_sum([10, 15, 3, 7], 17) == True

def test_two_sum_basic_false():
    """Test that function returns False when no two numbers sum to target."""
    assert two_sum([1, 2, 3, 4], 10) == False
    assert two_sum([5, 6, 7, 8], 20) == False

def test_two_sum_edge_cases():
    """Test edge cases like empty list and single element list."""
    assert two_sum([], 5) == False
    assert two_sum([5], 10) == False

def test_two_sum_zero_target():
    """Test scenarios with zero as the target."""
    assert two_sum([-1, 1, 2, 3], 0) == True
    assert two_sum([1, 2, 3], 0) == False

def test_two_sum_negative_numbers():
    """Test scenarios with negative numbers."""
    assert two_sum([-5, -2, 0, 2, 5], 0) == True
    assert two_sum([-10, -5, 0, 5, 10], 7) == False

def test_two_sum_large_numbers():
    """Test scenarios with large numbers."""
    assert two_sum([1000000, 2000000, 3000000], 3000000) == True

def test_two_sum_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        two_sum("not a list", 5)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        two_sum([1, 2, "3", 4], 5)

def test_two_sum_duplicate_numbers():
    """Test error handling for lists with duplicate numbers."""
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        two_sum([1, 2, 2, 3], 4)