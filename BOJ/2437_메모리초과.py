from itertools import *

n = int(input())
c = list(map(int, input().split()))

c.sort()
c2 = set()

cnt = n
for i in range(n):
    t = list(combinations(c, cnt))
    cnt -= 1

    for k in t:
        c2.add(sum(k))

c2 = list(c2)

for i in range(len(c2)):
    if c2[i+1] - c2[i] != 1:
        print(c2[i]+1)
        break




