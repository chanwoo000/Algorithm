n = int(input())

arr = [int(input()) for i in range(n)]
arr.sort()
mnum = 1000


for i in range(n):
    cnt = 0
    for j in range(arr[i],arr[i]+5):
        if j not in arr:
            cnt += 1
    mnum = min(mnum,cnt)

print(mnum)


