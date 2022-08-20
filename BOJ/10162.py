n = int(input())

t = [300, 60, 10]

cnt = 0

if (n % t[2]) != 0:
    print(-1)
    exit()

tt = []
for i in t:
    tt.append(n // i)
    n = n % i

print(*tt)