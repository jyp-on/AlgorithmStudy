N = int(input())

a = [0]*1000001
a[1], a[2] = 1, 2
for i in range(3, N+1):
    a[i] = (a[i-2] + a[i-1]) % 15746
print(a[N])


