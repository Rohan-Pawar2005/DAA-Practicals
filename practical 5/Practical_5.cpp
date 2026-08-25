# Knapsack function
def knapsack(capacity, weight, value, n):
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(n + 1):
        for w in range(capacity + 1):

            if i == 0 or w == 0:
                dp[i][w] = 0

            elif weight[i - 1] <= w:
                dp[i][w] = max(
                    value[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main function
def main():
    n = int(input("Enter number of items: "))

    print("Enter weights of sack:")
    weight = list(map(int, input().split()))

    print("Enter profits corresponding to their sack weight:")
    value = list(map(int, input().split()))

    capacity = int(input("Enter knapsack capacity: "))

    result = knapsack(capacity, weight, value, n)

    print("Maximum profit =", result)


# Call main function
if __name__ == "__main__":
    main()