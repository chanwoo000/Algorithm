import math

N = int(input())
crains = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
crains.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0]>crains[0] : print(-1)
else :
    maxcount = mincount = math.ceil(M/N)
    idx, count = 0, 0
    for i, crain in enumerate(crains[1:], start=1):
        count = 0
        while idx<M and (crain<boxes[idx] or count<mincount) :
            idx+=1
            count+=1
        if idx/i > maxcount : maxcount=math.ceil(idx/i)
    print(maxcount)