import sys
n = int(input())
s = []

for i in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'add':
        m = int(cmd[1])
        if m not in s:
            s.append(m)

    elif cmd[0] == 'check':
        m = int(cmd[1])
        print(1 if m in s else 0)

    elif cmd[0] == 'remove':
        m = int(cmd[1])
        if m in s:
            s.remove(m)

    elif cmd[0] == 'toggle':
        m = int(cmd[1])
        if m in s:
            s.remove(m)
        else:
            s.append(m)

    elif cmd[0] == 'all':
        s = list(range(1, 21))

    elif cmd[0] == 'empty':
        s = []
