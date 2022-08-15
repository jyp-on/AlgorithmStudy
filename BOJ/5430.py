import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    q = deque()
    iserr = False
    reverse_cnt = 0
    패턴 = list(input())
    n = int(input().rstrip())
    배열 = input()

    배열 = 배열[1:len(배열)-2]
    배열 = 배열.split(',')

    for i in 배열:
        if i != '':
            q.append(i)

    for p in 패턴:
        if p != '\n':
            if p == 'R':
                reverse_cnt += 1
            else:
                if len(q) == 0:
                    print('error')
                    iserr = True
                    break
                else:
                    if reverse_cnt % 2 == 0:
                        q.popleft()
                    else:
                        q.pop()
    if reverse_cnt % 2 == 1:
        q.reverse()

    if iserr == False:
        print('[', end='')
        s = ''
        for i in q:
            s += i
            s += ','
        s = s[:-1]
        print(s, end='')
        print(']')
