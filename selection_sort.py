def selection_sort(arr):
    """
    Sorts a list of numbers using the Selection Sort algorithm.
    
    Time Complexity: O(n^2)
    """
    n = len(arr)
    # Outer loop: Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        
        # Inner loop: Check elements from the current position 'i' to the end
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the element at the current position 'i'
        temp = arr[i]
        # Assign the second value to the first position
        arr[i] = arr[min_idx]
        # Assign the stored first value to the second position
        arr[min_idx] = temp
    
    return arr
