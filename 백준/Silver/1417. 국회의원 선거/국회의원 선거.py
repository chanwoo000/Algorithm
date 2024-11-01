n = int(input())
votes = []
cnt = 0

for _ in range(n):
    votes.append(int(input()))

while votes.index(max(votes)) != 0:
    votes[votes.index(max(votes))] -= 1
    votes[0] += 1
    cnt += 1

for i in range(1, n):
    if votes[0] == votes[i]:
        votes[i] -= 1
        votes[0] += 1
        cnt += 1
print(cnt)