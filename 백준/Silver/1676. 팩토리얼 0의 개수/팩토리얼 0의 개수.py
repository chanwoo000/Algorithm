a = int(input())
fac = 1
cnt = 0

for i in range(1,a+1):
    fac *= a
    a -= 1
fac1 = str(fac)

for i in reversed(range(len(fac1))):
    if fac1[i] == '0':
        cnt += 1
    else:
        break

print(cnt)