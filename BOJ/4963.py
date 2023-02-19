import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def dfs(y, x):
    visited[y][x] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<col and 0<=ny<row:
            if graph[ny][nx] != 0 and not visited[ny][nx]:
                dfs(ny, nx)

while True:
    col, row = map(int, input().split())
    if col == 0 and row == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0]*col for _ in range(row)]

    cnt = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                if not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
    print(cnt)