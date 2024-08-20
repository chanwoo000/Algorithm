import sys
a = int(input())
num = []
for i in range(a):
    num.append(int(sys.stdin.readline()))

result = list(set(num))
result.sort()
for i in result:
    print(i)