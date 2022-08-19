import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

prefix_sum = [0] #누적합의 0번인덱스는 보기편하게 하기위해 0으로 고정

t = 0
for i in num:
    t += i
    prefix_sum.append(t)

for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])