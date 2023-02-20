from collections import deque
import sys
input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]
def bfs(x, y, e_x, e_y):
    visited[y][x] = 1
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<l and 0<=nx<l:
                if graph[ny][nx] == 0:
                    if not visited[ny][nx]:
                        graph[ny][nx] = graph[y][x] + 1
                        q.append((ny, nx))

T = int(input())
for i in range(T):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    visited = [[0]*l for _ in range(l)]
    s_x, s_y = map(int, input().split()) # 시작
    e_x, e_y = map(int, input().split()) # 목표
    bfs(s_x, s_y, e_x, e_y)
    print(graph[e_y][e_x])
