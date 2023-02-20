import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    global temp_cnt
    temp_cnt += 1
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<m and 0<=nx<n:
            if graph[ny][nx] == 0 and not visited[ny][nx]:

                dfs(ny, nx)


m, n, k = map(int, input().split()) # row == m , col == n
graph = [[0]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(k):
    a_x, a_y, b_x, b_y = map(int, input().rstrip().split())
    for o in range(a_y, b_y):
        for z in range(a_x, b_x):
            graph[o][z] = 1

cnt = 0
area_list = []
for i in range(m):
    for k in range(n):
        if graph[i][k] == 0:
            if not visited[i][k]:
                temp_cnt = 0
                dfs(i, k)
                area_list.append(temp_cnt)
                cnt += 1

print(cnt)
for i in sorted(area_list):
    print(i, end=' ')

