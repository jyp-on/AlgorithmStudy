n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    for row in range(i-1, x):
        ans += sum(arr[row][j-1:y])
    print(ans)