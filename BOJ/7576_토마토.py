import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])



def bfs():
    global ans
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])

bfs()
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans-1) # 처음시작이 1임.



