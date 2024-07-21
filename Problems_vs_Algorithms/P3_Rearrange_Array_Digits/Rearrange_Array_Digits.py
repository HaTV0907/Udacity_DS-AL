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

def rearrange_digits(input_list):
    if None == input_list:
        print("None input_list")
        return [-1]
    if 0 == len(input_list):
        print("empty input_list")
        return [-1]
    # Step 1: Sort the input list using merge sort
    merge_sort(input_list)

    # Step 2: Create two numbers
    num1 = ''
    num2 = ''
    
    # Step 3: Alternate adding digits to num1 and num2
    for index, digit in enumerate(input_list):
        if index % 2 == 0:
            num1 += str(digit)
        else:
            num2 += str(digit)

    # Step 4: Convert to integers and return
    return int(num1), int(num2)

# Test the function with the provided test cases
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([None, [-1]])
test_function([[], [-1]])

