import sys
input = sys.stdin.readline

N = int(input())

t = [[0]*2 for i in range(N)]

for i in range(N):
    start, end = map(int, input().split())
    t[i][0] = start
    t[i][1] = end

t.sort(key = lambda x : (x[1], x[0])) # -> 2번쨱값으로 먼저 정렬후 첫번째 값으로 정렬

temp = 0
a = 0

for start, end in t:
    if start >= temp:
        a += 1
        temp = end
print(a)