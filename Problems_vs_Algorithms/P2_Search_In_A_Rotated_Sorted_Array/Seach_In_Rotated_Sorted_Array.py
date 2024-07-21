def rotated_array_search(input_list = None, number = None):
    if None == input_list or None == number:
        return -1 # iuvalid param
    left = 0
    right = len(input_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the mid element is the target
        if input_list[mid] == number:
            return mid
        
        # Determine which side is sorted
        if input_list[left] <= input_list[mid]:  # Left side is sorted
            if input_list[left] <= number < input_list[mid]:  # Target in left side
                right = mid - 1
            else:  # Target in right side
                left = mid + 1
        else:  # Right side is sorted
            if input_list[mid] < number <= input_list[right]:  # Target in right side
                left = mid + 1
            else:  # Target in left side
                right = mid - 1
                
    return -1  # Target not found


print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 7))  # Output: 3
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 4))  # Output: 0
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 2))  # Output: 6
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2]))  # Output: -1
print(rotated_array_search(None, 3))  # Output: -1
print(rotated_array_search(None, None))  # Output: -1