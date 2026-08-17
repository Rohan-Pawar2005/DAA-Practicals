import time

# Recursive function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# User input
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    start_time = time.perf_counter()

    result = factorial_recursive(n)

    end_time = time.perf_counter()

    print("\n--- Recursive Method ---")
    print("Factorial =", result)
    print("Execution Time =", end_time - start_time, "seconds")
    print("Time Complexity = O(n)")
    print("Space Complexity = O(n)")