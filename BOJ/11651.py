N = int(input())

좌표들 = []
for _ in range(N):
    x, y = map(int, (input().split()))
    좌표들.append([x, y])


#정렬전에 좌표 x, y를 뒤집음
for i in range(len(좌표들)):
    좌표들[i][0] , 좌표들[i][1] = 좌표들[i][1], 좌표들[i][0]

정렬 = sorted(좌표들)

for i in range(len(좌표들)):
    좌표들[i][0] , 좌표들[i][1] = 좌표들[i][1], 좌표들[i][0]

for i in 정렬:
    print(i[0], i[1])