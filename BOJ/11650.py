N = int(input())

좌표들 = []
for _ in range(N):
    x, y = map(int, (input().split()))
    좌표들.append([x, y])

정렬 = sorted(좌표들)

for i in 정렬:
    print(i[0], i[1])


