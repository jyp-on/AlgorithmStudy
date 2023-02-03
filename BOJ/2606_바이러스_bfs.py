from collections import defaultdict
from collections import deque

n = int(input())
connect_len = int(input())

dic = defaultdict(list)
for i in range(connect_len):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a) # 양방향

# bfs 접근

visited = [False for _ in range(n+1)] # 1번부터 시작하기 위해 n+1

q = deque()
q.append(1)

while q:
    v = q.popleft()

    visited[v] = True

    for k in dic[v]:
        if not visited[k]:
            q.append(k)

print(visited.count(True)-1)

