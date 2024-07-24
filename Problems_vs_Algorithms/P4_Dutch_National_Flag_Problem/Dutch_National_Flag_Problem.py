def sort_012(input_list = None):
    """
    Given an input array consisting of only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list (list): List to be sorted
    """
    if None == input_list:
        print("Invalid param")
        return [-1]
    if 0 == len(input_list):
        print("Empty list")
        return []
    low = 0  # Pointer for the next position of 0
    mid = 0  # Pointer for the current element
    high = len(input_list) - 1  # Pointer for the next position of 2

    while mid <= high:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]  # Swap
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:  # input_list[mid] == 2
            input_list[mid], input_list[high] = input_list[high], input_list[mid]  # Swap
            high -= 1
    return input_list
# Example test cases
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("sorted_array: " + str(sorted_array))
        print("expected: " + str(sorted(test_case)))
        print("Fail")

# Testing the function
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
sort_012() # invalid param
test_function([]) 
test_function() # error
