n = int(input())
cnt = [0] * 91
cnt[0] = 0
cnt[1] = 1
for i in range(2,n+1):
  cnt[i] = cnt[i-2] + cnt[i-1]
  
print(cnt[n])


