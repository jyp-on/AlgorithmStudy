import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1

for num in arr:
    if target < num:
        break

    target += num

print(target)

# 1 1 2
# 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 1 + 1 + 2 = 4
#
# 3추가하면
#
# 1+3 = 4 (최소)
# 4+3 = 7 (최대)
#
# 결국 새로추가한거 3 + 기존 최소 1
# 가 최소
#
# 1 1 2 에 5추가하면
#
# 4 + 5 = 9 (최대)
# 1 + 5 = 6 (최소)
# 즉 1~4 구간에 6~9가 추가됬으므로
# 5가 없음

