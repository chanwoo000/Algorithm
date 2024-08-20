a = int(input())
chan = []
for i in range(a):
    chan.append(input())

result = list(set(chan))
result.sort(key = lambda x : (len(x),x))

for i in result:
    print(i)

