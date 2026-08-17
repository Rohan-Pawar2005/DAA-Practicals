import time

# Insertion Sort Function
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Main Program
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)

# Measure execution time
start_time = time.perf_counter()

insertion_sort(arr)

end_time = time.perf_counter()

# Display the sorted array
print("\nSorted Array:", arr)

# Display execution time
print(f"Execution Time: {end_time - start_time:.10f} seconds")

# Display time complexity
print("\nTime Complexity of Insertion Sort:")
print("Best Case   : O(n)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")
