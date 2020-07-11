# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here  
        while cur_index < len(arr):
            if arr[smallest_index] > arr[cur_index]:
                smallest_index = cur_index
            cur_index += 1               
        

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] =  arr[smallest_index], arr[i]       

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    total =  len(arr)
    for i in range(0, total - 1):
        for j in range(0, total - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]    
       

    return arr


print(selection_sort([2,8,5,3,9,4,1]))
print(bubble_sort([2,8,5,3,9,4,1]))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen i in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
   
    if arr:

        # Check negative number
        if min(arr) < 0:
            return "Error, negative numbers not allowed in Count Sort"

        # Get maximum number.
        if maximum is None:
            maximum = max(arr)

        # Create count array intialize with zero.
        count_arr = [0] * ( maximum + 1 )
        
        # Store the count of each number in count array.
        for i in range(0, len(arr)):
            count_arr[arr[i]] += 1   

        # Modify the count array by adding previous counts
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1] 

        # Place the number on their correct postion and decrease the count by one.
        sort_arr = [0] * len(arr)
        
        for num in arr: 
            # return num
            count_arr[num] -= 1
            sort_arr[count_arr[num]] = num
            
        return sort_arr
    else:
        return arr    

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr = [3, 2, 1]
print(counting_sort(arr))
