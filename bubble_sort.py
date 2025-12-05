def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop: Controls how many passes are needed (n-1 passes).
    for i in range(n - 1):
        
        # Inner loop: Compares and swaps adjacent elements in the unsorted portion.
        # The '- i' ensures we don't check the largest elements that have already "bubbled up" 
        # to the end of the list in previous passes.
        for j in range(n - 1 - i):
            
            # If the element on the left is greater than the element on the right...
            if arr[j] > arr[j + 1]:
                
                # 1. Store the value of the first element in a temporary variable
                temp = arr[j]
                # 2. Overwrite the first element's position with the second element's value
                arr[j] = arr[j + 1]
                # 3. Overwrite the second element's position with the original first element's value (from temp)
                arr[j + 1] = temp            
    return arr

# Example Usage:
# data = [5, 1, 4, 2, 8]
# simple_bubble_sort(data) 
# print(data) # Output: [1, 2, 4, 5, 8]


def main():
    """
    Main function to test the Selection Sort and Bubble Sort implementations.
    """
    # Define an unsorted list for testing
    original_list = [64, 25, 12, 22, 11, 90, 15, 7]
    
    print(f"Original List: {original_list}")
    print("-" * 30)
    
    # 1. Test Selection Sort
    # Create a copy of the list to keep the original untouched
    list_for_selection = original_list[:] 
    
    sorted_by_selection = selection_sort(list_for_selection)
    print(f"**Selection Sort** Result: {sorted_by_selection}")
    
    print("-" * 30)
    
    # 2. Test Bubble Sort
    # Create a fresh copy of the list
    list_for_bubble = original_list[:] 
    
    sorted_by_bubble = bubble_sort(list_for_bubble)
    print(f"**Bubble Sort** Result: {sorted_by_bubble}")

# Execute the main function
if __name__ == "__main__":
    main()
