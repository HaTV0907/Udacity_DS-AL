def merge_sort(arr):
    if None == arr:
        print("None arr")
        return -1
    if 0 == len(arr):
        print("empty arr")
        return -1
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array elements
        right_half = arr[mid:]

        merge_sort(left_half)  # Sort the first half
        merge_sort(right_half)  # Sort the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:  # Change to descending order
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def get_min_max(ints = None):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if None == ints:
        print("Invalid params")
        return -1
    if 0 == len(ints):
        print("empty arr")
        return -1
    sorted_arr = merge_sort(ints)
    print(sorted_arr)
    return (sorted_arr[len(sorted_arr) - 1], sorted_arr[0]) 

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if -1 == get_min_max([]) else "Fail")
print ("Pass" if -1 == get_min_max() else "Fail")
