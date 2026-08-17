import time

# Selection Sort Function
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the index of the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Main Program
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)

# Measure execution time
start_time = time.perf_counter()

selection_sort(arr)

end_time = time.perf_counter()

# Display the sorted array
print("\nSorted Array:", arr)

# Display execution time
print(f"Execution Time: {end_time - start_time:.10f} seconds")

# Display time complexity
print("\nTime Complexity of Selection Sort:")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")
