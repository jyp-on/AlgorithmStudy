n = int(input())
n = 1000 - n
coin = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in coin:
    if n == 0:
        break
    cnt += n // i
    n = n % i
print(cnt)