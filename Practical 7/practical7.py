def combCoin(coin, n):
    m = len(coin)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Amount 0 can always be formed in 1 way
    for i in range(m + 1):
        dp[i][0] = 1
    for j in range(1, n + 1):
        dp[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if coin[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            else:
                dp[i][j] = (dp[i - 1][j]  + dp[i][j - coin[i - 1]])

    return dp[m][n]

amount = int(input("Enter the amount you want to pay: "))

n = int(input("Enter the number of variants of the coin: "))

coin = []

print("Enter the variants of the coin:")

for i in range(n):
    value = int(input())
    coin.append(value)

result = combCoin(coin, amount)

print("Number of ways to give the amount is:", result)
