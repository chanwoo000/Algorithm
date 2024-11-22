import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline 

n,m = map(int,input().split())
p = list(range(n+1)) 


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x,y):
    px = find(x)
    py = find(y)
    if x <= y:
        p[py] = px
    else:
        p[px] = py
        
def sol():
    res = [] 
    for _ in range(m):
        c,a,b = map(int,input().split())
        if c == 0: 
            union(a,b)
        else:
            if find(a) == find(b):
                res.append("YES")
            else:
                res.append("NO")
    print(*res,sep="\n")

sol()