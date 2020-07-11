def linear_search(arr, target):
    # Your code here
    for index, num in enumerate(arr):
        if num == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    arr.sort()

    low, high = 0, len(arr)-1
    
    while low <= high:
        
        mid = ( low + high ) // 2
        
        if target == arr[mid]:
            return mid

        elif target < arr[mid]:
            high = mid-1

        elif target > arr[mid]:
            low = mid +1     

    return -1  # not found

# Linear Search
# arr = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# print(linear_search(arr, -6))

# Binary Search
# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# arr = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# print(binary_search(arr, -6))
