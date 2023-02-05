import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if not visited[n]:
            visited[n] = visited[node] + 1
            dfs(n)

n = int(input())
graph = [[] for _ in range(n+1)]
s, target = map(int, input().split())

for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
dfs(s)
print(visited[target] if visited[target] > 0 else -1)