cnt = 0
while True:
    l,p,v = map(int, input().split())
    if (p == 0):
        break

    몫 = v // p
    나머지 = min(v % p, l)
    cnt += 1
    print(f'Case {cnt}: {(l*몫) + 나머지}')

