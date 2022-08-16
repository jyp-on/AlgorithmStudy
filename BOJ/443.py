import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lan = [int(input()) for _ in range(K)]

start = 1
end = max(lan)

랜선최대길이 = 0

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in lan:
        sum += i // mid
    if sum >= N:
        start = mid + 1
        랜선최대길이 = mid
    else:
        end = end-1
print(랜선최대길이)
