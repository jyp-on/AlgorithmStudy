import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

N = int(input())

for _ in range(N):
    order = input().split()
    if 'push' in order[0]:
        queue.append(int(order[1]))
    elif 'front' in order[0]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in order[0]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif 'size' in order[0]:
        print(len(queue))
    elif 'empty' in order[0]:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'pop' in order[0]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())