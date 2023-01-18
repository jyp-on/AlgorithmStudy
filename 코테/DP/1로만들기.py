x = int(input())

d = [0] * 30001

#  점화식 끝에 1을 더해주는 이유는 함수의 호출 횟수를 구해야 하기때문.

for i in range(2, x+1):
    #  현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    #  현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])