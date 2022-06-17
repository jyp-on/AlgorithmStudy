N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
result = 0

for i in range(N): #0~4
    for j in range(i+1, N): #0~3
        for k in range(j+1, N): #0~2
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)





