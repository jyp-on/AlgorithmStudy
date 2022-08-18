T = int(input())
N = [0] * 101
for _ in range(T):
    N = [0] * 101
    N[1] = 1
    N[2] = 1
    N[3] = 1
    n = int(input())
    for i in range(4, n+1):
        N[i] = N[i-2] + N[i-3]

    print(N[n])
