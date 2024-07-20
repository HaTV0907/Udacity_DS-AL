import numpy as np
import math

def get_floor_value(number = None):
    if None == number:
        return -1
    return math.floor(number)

def square_root(numbers = None):
    if None == numbers:
        return -1
    if numbers < 0:
        print("Negative numbers can not have square root")
        return -1
    return get_floor_value(np.sqrt(numbers))

# Example usage
print(square_root(16))  # Output: 4.0
print(square_root(-16))  # Output: return -1
print(square_root(27))  # Output: 5.0
print(square_root(0))  # Output: 0
print(square_root())  # Output: -1
print(square_root(None))  # Output: -1
print(square_root(99999999))