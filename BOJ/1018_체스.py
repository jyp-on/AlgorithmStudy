N, M = int(input().split())

cnt = 0

for _ in range(N):
    row = input()
    for i in range(len(row)):
        if row[i] == row[i+1]:
            cnt += 1




