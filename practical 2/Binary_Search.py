import time

# Binary Search Function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Sorted array
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
target = int(input("enter the element to search:"))

# Start measuring execution time
start_time = time.perf_counter()

# Perform Binary Search
result = binary_search(arr, target)

# End measuring execution time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display Result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")

print(f"Execution Time: {execution_time:.10f} seconds")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")