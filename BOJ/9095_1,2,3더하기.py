# n이 3보다 클때 f(n) = f(n-1) + f(n-2) + f(n-3)
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(2)
        continue
    if n == 3:
        print(4)
        continue
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, len(d)):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])
