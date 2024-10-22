word1 = list(input())  
word2 = list(input())  

# LCS 테이블을 0이 아닌 문자열로 초기화
lcs = [['' for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]


for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i-1] == word2[j-1]:  
            lcs[i][j] = lcs[i-1][j-1] + word1[i-1]
        else:  
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]

lcs_string = lcs[len(word1)][len(word2)]
print(len(lcs_string))  
print(lcs_string)  
