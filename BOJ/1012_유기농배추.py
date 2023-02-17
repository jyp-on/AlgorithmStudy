import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    col, row, k = map(int, input().rstrip().split())
    graph = [[0 for _ in range(col)] for _ in range(row)]
    for _ in range(k):
        c, r = map(int, input().rstrip().split())
        graph[r][c] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    ans = 0

    def dfs(y, x):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < row and 0 <= nx < col:
                if graph[ny][nx] == 1:
                    graph[ny][nx] -= 1
                    dfs(ny, nx)

    for x in range(col):
        for y in range(row):
            if graph[y][x] == 1:
                dfs(y, x)
                ans += 1
    print(ans)





