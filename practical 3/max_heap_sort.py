import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def max_heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Input
arr = list(map(int, input("Enter the elements separated by spaces: ").split()))

print("\nOriginal Array:")
print(arr)

# Calculate execution time
start_time = time.perf_counter()

max_heap_sort(arr)

end_time = time.perf_counter()

print("\nSorted Array using Max Heap Sort:")
print(arr)

print("\nExecution Time:", end_time - start_time, "seconds")
print("Time Complexity: O(n log n)")
print("Space Complexity: O(log n) due to recursive heapify")