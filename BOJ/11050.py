def fact(n):
    fac = 1
    while n != 0:
        fac*=n
        n-=1
    return fac

n, k = map(int, input().split())
print(int(fact(n) / ( fact(n-k) * fact(k))))