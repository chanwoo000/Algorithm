n = int(input())
time = []
for i in range(n):
    time.append(tuple(map(int,input().split())))

time.sort(key = lambda x : x[1],reverse=True) #x[1]번째로 정렬하기
now = time[0][1]
for i in range(n):
    if now > time[i][1]:
        now = time[i][1] #now가 마감 시간보다 크면 마감시간에 맞춰 now 를 업데이트하기
    task = time[i][0]
    now = now - task    
    
if now < 0:
    print(-1)
else:
    print(now)