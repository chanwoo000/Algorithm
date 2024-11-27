import sys
n = int(input())
time = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    time.append((a, b))

time.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1]

for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)