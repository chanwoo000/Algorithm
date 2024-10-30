import sys
n = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0]*arr[k][1]*arr[j][1])
print(dp[0][-1])
