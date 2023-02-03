from collections import defaultdict

n = int(input())
connect_len = int(input())

dic = defaultdict(list)
for i in range(connect_len):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a) # 양방향

# dfs 접근

visited = [False for _ in range(n+1)] # 1번부터 시작하기 위해 n+1
def dfs(v, visited):
    global cnt
    if visited[v]:
        return

    visited[v] = True
    for k in dic[v]:
        if not visited[k]:
            dfs(k, visited)


dfs(1, visited)
print(visited.count(True)-1)