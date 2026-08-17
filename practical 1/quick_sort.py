import time

# Partition Function
def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort Function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Sort left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Main Program
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input(f"Element {i + 1}: ")))

# Start timer
start_time = time.perf_counter()

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

# End timer
end_time = time.perf_counter()

# Output
print("\nSorted Array:", arr)
print(f"Execution Time: {end_time - start_time:.10f} seconds")

print("\nTime Complexity of Quick Sort:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n^2)")
print("Space Complexity:")
print("Average Case: O(log n)")
print("Worst Case  : O(n)")
