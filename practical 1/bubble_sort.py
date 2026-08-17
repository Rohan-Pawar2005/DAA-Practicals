import time

# Bubble Sort Function
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if the array is already sorted
        if not swapped:
            break

# Main Program
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)

# Measure execution time
start_time = time.perf_counter()

bubble_sort(arr)

end_time = time.perf_counter()

# Display results
print("\nSorted Array:", arr)
print(f"Execution Time: {end_time - start_time:.10f} seconds")

# Time Complexity
print("\nTime Complexity of Bubble Sort:")
print("Best Case   : O(n)")
print("Average Case: O(n^2)")
print("Worst Case  : O(n^2)")
print("Space Complexity: O(1)")
