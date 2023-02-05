from collections import deque

N = int(input())
graph = []
MAX_arr = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    MAX_arr = max(MAX_arr, max(temp))
    graph.append(temp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(y, x, value, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] > value and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))


result = 0
for i in range(MAX_arr):
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)
