import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
def dfs(row, col, color):
    visited[row][col] = 1
    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[ny][nx] == color and not visited[ny][nx]:
                dfs(ny, nx, color)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0
for i in range(n):
    for k in range(n):
        if not visited[i][k]:
            dfs(i, k, graph[i][k])
            cnt += 1

print(cnt)

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for k in range(n):
        if graph[i][k] == 'G':
            graph[i][k] = 'R'

cnt = 0
for i in range(n):
    for k in range(n):
        if not visited[i][k]:
            dfs(i, k, graph[i][k])
            cnt += 1

print(cnt)