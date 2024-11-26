import sys
n = int(input())
tmp = []

for i in range(n):
    a = int(input())
    arr = []
    for j in range(a):
        b,c = map(int,sys.stdin.readline().split())
        arr.append((b,c))
    arr.sort(key=lambda x : x[0])
    two = arr[0][1]
    cnt = 1
    for k in range(1,a):
        if arr[k][1] < two :
            two = arr[k][1]
            cnt += 1
    print(cnt)

