import time

# Iterative function
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# User input
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    start_time = time.perf_counter()

    result = factorial_iterative(n)

    end_time = time.perf_counter()

    print("\n--- Iterative Method ---")
    print("Factorial =", result)
    print("Execution Time =", end_time - start_time, "seconds")
    print("Time Complexity = O(n)")
    print("Space Complexity = O(1)")