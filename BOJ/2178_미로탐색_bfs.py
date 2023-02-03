from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append((0, 0))

while queue: # bfs
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((ny, nx))
        else:
            continue


print(graph[-1][-1])





