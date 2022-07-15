T = int(input())

for i in range(T):
    t, s = input().split()
    t = int(t)

    for n in range(len(s)):
        for k in range(t):
            print(s[n], end='')
    print()