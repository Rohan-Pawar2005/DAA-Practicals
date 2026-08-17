import time

# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if element is found
    return -1  # Return -1 if element is not found


# Example array
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
target = int(input("enter the element to search:"))

# Start measuring execution time
start_time = time.perf_counter()

# Perform Linear Search
result = linear_search(arr, target)

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
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")