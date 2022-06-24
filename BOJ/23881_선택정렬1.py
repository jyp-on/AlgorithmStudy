import sys
input = sys.stdin.readline

length, cnt = map(int, input().split())

num = list(map(int, input().split()))

temp_cnt = 0

for k in range(length-1,0,-1): # 맨끝부터 점차 줄어듬
    temp_max = max(num[0:k+1])
    index = num.index(temp_max)

    if temp_max != num[k]: #제일 큰 숫자가 last가 아니면
        num[index], num[k] = num[k], num[index]
        temp_cnt += 1
        if temp_cnt == cnt:
            print(num[index], num[k])
            sys.exit()

if temp_cnt < cnt:
    print(-1)


