import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):
    order = input().rstrip().split(' ')
    if len(order) == 1:
        if order[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
        continue

    o, n = order[0], int(order[1])

    if 'add' == o:
        if n not in S:
            S.add(n)
    elif 'check' == o:
        print(1 if n in S else 0)
    elif 'remove' == o:
        if n in S:
            S.discard(n)
    elif 'toggle' == o:
        if n in S:
            S.discard(n)
        else:
            S.add(n)
