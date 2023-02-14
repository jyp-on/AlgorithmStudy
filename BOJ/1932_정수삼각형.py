n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, len(t)):
    t[i][0] += t[i-1][0]
    t[i][-1] += t[i-1][-1]
for i in range(2, len(t)):
    for k in range(1, len(t[i])-1):
        t[i][k] += max(t[i-1][k-1], t[i-1][k])
print(max(t[-1]))

