from collections import deque
n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

# 모든 인덱스를 확인하여 1이 있으면 bfs로 지난부분 0으로 만들기., 다 파고들면 다시 방문안한 1부터 dfs

house = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(r, c):
    q = deque()
    q.append((r, c))

    graph[r][c] = 0

    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                cnt += 1
                graph[ny][nx] = 0
                q.append((ny, nx))
            else:
                continue

    return cnt


for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house.append(bfs(r, c))
            # for i in graph: # 확인.
            #     print(i)


house.sort()
print(len(house))
for h in house:
    print(h)