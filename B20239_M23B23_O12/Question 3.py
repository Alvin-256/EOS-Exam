# Using the Bubble Sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Using the Quick Sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

unsorted_list = [14, 27, 8, 42, 11, 35, 9, 56, 23]

# Sorting using the Bubble Sort
bubble_sort_result = unsorted_list.copy()
bubble_sort(bubble_sort_result)
print("Bubble Sort Result:", bubble_sort_result)
# The Bubble Sort Result: [8, 9, 11, 14, 23, 27, 35, 42, 56]

# Sorting using the Quick Sort
quick_sort_result = quick_sort(unsorted_list.copy())
print("Quick Sort Result:", quick_sort_result)
# The Quick Sort Result: [8, 9, 11, 14, 23, 27, 35, 42, 56]

# The Complexity Class of the Bubble Sort is O(n^2)
# The Complexity Class of the Quick Sort is O(n log n)


