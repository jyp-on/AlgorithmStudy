n, l = map(int, input().split())

p = list(map(int, input().split()))
p.sort()

start = p[0]
end = p[0] + l #테이프의 길이만큼 더함.

cnt = 1 # 1개의 테이프를 붙이고 시작하기때문에 1개.

for i in range(n):
    if start <= p[i] < end:
        continue
    else:
        start = p[i]
        end = p[i] + l
        cnt += 1
print(cnt)