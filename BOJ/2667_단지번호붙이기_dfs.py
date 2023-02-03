n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

# 모든 인덱스를 확인하여 1이 있으면 dfs로 지난부분 0으로 만들기., 다 파고들면 다시 방문안한 1부터 dfs

house = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 1  # 처음 들어가자마자 0으로 없애줌.

def dfs(y, x):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
            global cnt
            cnt += 1
            graph[ny][nx] = 0
            dfs(ny, nx)
        else:
            continue

    return cnt

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            graph[r][c] = 0
            house.append(dfs(r, c))
            cnt = 1
            # for i in graph: # 확인.
            #     print(i)
            # print('\n')


house.sort()
print(len(house))
for h in house:
    print(h)