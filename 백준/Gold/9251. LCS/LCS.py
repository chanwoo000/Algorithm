word1 = list(input())
word2 = list(input())
lcs = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1] == word2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            
print(lcs[len(word1)][len(word2)])