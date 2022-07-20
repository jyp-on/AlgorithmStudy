import sys
input = sys.stdin.readline

N, M = map(int, input().split())

듣도 = []
for _ in range(N):
    듣도.append(input().strip())
듣도 = set(듣도)



보도 = []
for _ in range(M):
    보도.append(input().strip())
보도 = set(보도)

듣도보도 = 듣도 & 보도

듣도보도 = sorted(list(듣도보도))

print(len(듣도보도))
for i in 듣도보도:
    print(i)


