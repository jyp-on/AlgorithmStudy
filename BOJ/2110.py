n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
답 = 0

while start <= end:
    mid = (start+end)//2 #공유기 사이 거리
    now = arr[0]
    공유기수 = 1

    for i in range(1, len(arr)):
        if arr[i] >= now + mid: #current와
            공유기수 += 1
            now = arr[i]

    if 공유기수 >= c:
        start = mid + 1
        답 = mid
    else:
        end = mid -1

print(답)