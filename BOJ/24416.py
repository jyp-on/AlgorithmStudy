N = int(input())
cnt1 = 0
cnt2 = 0

def fib1(n):
    global cnt1

    if (n == 1) or (n == 2):
        cnt1 = cnt1 + 1
        return 1
    else:
        return (fib1(n-1) + fib1(n-2))


def fib2(n):
    global cnt2

    f[1],f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt2 += 1
    return f[n]

f = [0] * 41

fib1(N)
fib2(N)
print(cnt1)
print(cnt2)

