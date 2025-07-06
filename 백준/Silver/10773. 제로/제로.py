n = int(input())
arr = []
cnt = 0

for i in range(n):
  a = int(input())
  if a != 0:
    arr.append(a)
  else:
    arr.pop()

for i in range(len(arr)):
  cnt += arr[i]

print(cnt)
