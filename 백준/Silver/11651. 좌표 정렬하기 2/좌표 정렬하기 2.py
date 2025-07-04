n = int(input())
num = []
for i in range(n):
  a,b = (input().split())
  num.append([int(a),int(b)])
num.sort(key=lambda x : (x[1],x[0]))

for i in num:
  print(i[0],i[1])
