import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

coin = []
for _ in range(n):
    coin.append(int(input().rstrip()))

cnt = 0

for i in reversed(range(n)):
    cnt += k // coin[i]
    k = k % coin[i]

print(cnt)