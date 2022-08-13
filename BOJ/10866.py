import sys
from collections import deque
input = sys.stdin.readline

d = deque()

for i in range(int(input())):
    o = input().split()

    if o[0] == 'push_front':
        d.appendleft(o[1])
    elif o[0] == 'push_back':
        d.append(o[1])
    elif o[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif o[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif o[0] == 'size':
        print(len(d))
    elif o[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif o[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif o[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
