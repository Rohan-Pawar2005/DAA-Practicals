# Chain Matrix Multiplication using Dynamic Programming

def chain_matrix(p, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        dp[i][i] = 0
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):

                cost = (
                    dp[i][k] + dp[k + 1][j]+ p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]
    
#main 
n = int(input("Enter number of Matrix: "))
p = []
print("Enter the dimensions of the matrix:")
for i in range(n + 1):
    p.append(int(input()))
result = chain_matrix(p, n + 1)
print("Minimum Multiplication cost is:", result)