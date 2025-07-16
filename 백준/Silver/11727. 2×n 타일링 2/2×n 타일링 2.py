n = int(input())
dp = [0] * 1001
dp[0] = 1
for i in range(1,n):
  if i%2 == 0:
    dp[i] = (dp[i-1]*2) - 1
  else:
    dp[i] = (dp[i-1]*2) + 1

print(dp[n-1]%10007)
