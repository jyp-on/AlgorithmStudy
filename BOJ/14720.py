n = int(input())
milk = list(map(int,input().split()))

cnt = 0

for i in range(n):
    if milk[i] == cnt % 3: #cnt를 3으로 나눠준 값이랑 같으면 cnt를 1 늘려준다.
        cnt += 1

print(cnt)