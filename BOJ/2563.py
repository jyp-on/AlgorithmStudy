import sys
input = sys.stdin.readline
n = int(input())
arr = [[0]*101 for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    for row in range(x, x + 10):
        for col in range(y, y+10):
            arr[row][col] = 'X'

ans = 0
for i in arr:
    for j in i:
        if j == 'X':
            ans += 1
print(ans)