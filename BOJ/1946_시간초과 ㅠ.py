t = int(input())

for _ in range(t):
    n1 = []
    n2 = []
    for i in range(int(input())):
        o1 , o2 = map(int, input().split())
        n1.append(o1)
        n2.append(o2)
    idx_n1 = n1.index(min(n1))
    idx_n2 = n2.index(min(n2))
    cnt = 0
    for i in range(len(n1)):
        if (n2[i] <= n2[idx_n1]) & (n1[i] <= n1[idx_n2]):
            cnt += 1
    print(cnt)
