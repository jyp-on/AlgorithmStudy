n, m = map(int, input().split())

items = list(map(int, input().split()))

start = 0
end = max(items)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for item in items:
        if item > mid:
            total += item - mid
    if total > m:  # 떡볶이 양이 주문량보다 많을때
        start = mid + 1
    else:  # 떡볶이 양이 주문량보다 적을때
        end = mid - 1

print(mid)


