n = int(input())
A = list(map(int, input().split()))

d = [1] * n

for i in range(1, len(d)):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))