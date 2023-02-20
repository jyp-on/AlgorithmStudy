import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v # 부모저장.
            dfs(i)
dfs(1)
for i in visited[2:]:
    print(i)
