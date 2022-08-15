import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

q = deque()

for i in range(1, N+1):
    q.append(i)

cnt = 0
while True:
    if q[0] == a[0]: #찾는원소일떄 1번
        if len(a) == 1:
            break
        else:
            q.popleft()
            del a[0]

    else:
        if q.index(a[0]) <= int(len(q)/2): #왼쪽에 더 가까운경우
            q.append(q.popleft())
            cnt += 1
        else:
            q.appendleft(q.pop())
            cnt += 1
print(cnt)



