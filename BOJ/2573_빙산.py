from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

time = 0
def bfs(a, b):
    global time
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                #  바다인 경우
                if graph[ny][nx] == 0:
                    if graph[y][x] > 0:
                        graph[y][x] -= 1
                # 빙산인 경우
                elif graph[ny][nx] != 0:
                    # 빙산인 경우만 방문처리, 바다는 2개 이상의 빙산에게
                    # 영향을 끼칠 수 있으므로 방문처리하면 안됨.
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    time += 1

def checkBFS(a, b, visited):

    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] != 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

# 두 덩이 이상 갈라졌는지 체크.
def check():
    checkCnt = 0
    visited = [[0] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if graph[r][c] != 0 and not visited[r][c]:
                checkBFS(r, c, visited)
                checkCnt += 1

    return checkCnt

for r in range(n):
    for c in range(m):
        if graph[r][c] != 0:
            bfs(r, c)
            if check() >= 2:  # 빙산 몇 덩이인지 확인.
                print(time)
                exit()

print(0)