n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
s = 0
for i in range(n):
    max_b = max(b)
    s += (a[i] * max_b)
    b.remove(max_b)
print(s)