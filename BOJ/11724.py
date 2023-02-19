import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    visited[V] = 1
    for i in graph[V]:
        if not visited[i]:
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)