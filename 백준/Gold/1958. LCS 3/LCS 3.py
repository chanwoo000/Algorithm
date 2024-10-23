word1 = list(input())
word2 = list(input())
word3 = list(input())

dp = [[[0]*(len(word3)+1) for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

for i in range(1, len(word1)+1):
    for j in range(1, len(word2)+1):
        for k in range(1, len(word3)+1):
            if word1[i-1] == word2[j-1] == word3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(word1)][len(word2)][len(word3)])