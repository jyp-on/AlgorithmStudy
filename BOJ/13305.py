N = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = dist[0] * cost[0]
m = cost[0]

for i in range(1, N-1):
    if cost[i] < m:
        m = cost[i]
    ans += m * dist[i]
print(ans)