def two_sum(numbers: list[int], target: int) -> bool:
    """
    Determine if any two unique numbers in the input array sum to the target.
    
    Args:
        numbers (list[int]): A list of unique integers to check.
        target (int): The target sum to find.
    
    Returns:
        bool: True if any two numbers in the list sum to the target, False otherwise.
    
    Raises:
        TypeError: If input is not a list or contains non-integer values.
        ValueError: If the input list contains duplicate numbers.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for non-integer values
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Check for uniqueness 
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input list must contain unique integers")
    
    # Use a set for O(n) lookup
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False