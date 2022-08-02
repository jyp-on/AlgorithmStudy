N = int(input())

가로 = []
세로 = []

for _ in range(6):
    방향, 길이 = map(int, input().split())
    if 방향 == 1 or 방향 == 2:
        가로.append(길이)
    else: 세로.append(길이)
print((( max(가로)*max(세로) )- ( min(가로)*min(세로) ))* N)