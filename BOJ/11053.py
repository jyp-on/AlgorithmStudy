n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
for i in range(1, len(d)):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j]+1)

# print(d)
print(max(d))
target = max(d)

result = []
for i in range(n-1, -1, -1):
    if d[i] == target:
        result.append(arr[i])
        target -= 1

result.reverse()
for i in result:
    print(i, end=' ')