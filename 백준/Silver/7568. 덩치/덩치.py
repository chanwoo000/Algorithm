a = int(input())
person = []
arr = [0] * a  # 각 사람의 순위를 저장할 리스트, 초기값은 0으로 설정

for i in range(a):
    person.append(list(map(int, input().split())))

for i in range(a):
    cnt = 1  # 순위 계산을 위한 초기값
    for j in range(a):
        if i != j:
            if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
                cnt += 1  # i번째 사람보다 j번째 사람이 더 크거나 같으면 순위가 밀림
    arr[i] = cnt  # 최종 순위를 arr에 저장

print(*arr)
