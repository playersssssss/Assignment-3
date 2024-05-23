import numbers


def find_max_min(numbers):
    # Initialize max_value with negative infinity and min_value with positive infinity
    max_value = float('-inf')
    min_value = float('inf')

    # Iterate through the list of numbers
    for num in numbers:
        # Update max_value if num is greater
        if num > max_value:
            max_value = num
        # Update min_value if num is smaller
        elif num < min_value:
            min_value = num

    # Return min_value as minimum and max_value as maximum

    return min_value, max_value


# Example usage:
data = [15, 7, 28, 12, 35]
result = find_max_min(data)
print(f"Minimum value: {result[0]}, Maximum value: {result[1]}")
