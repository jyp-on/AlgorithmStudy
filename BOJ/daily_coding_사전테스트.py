n = int(input())

li = [[''] * n for i in range(n)]

# 65 ~ 90 -> A to Z  아스키코드

idx = 65
t = 0
switch = 'up'
for i in range(n):
    for _ in range(n):

        li[t][i] = chr(idx)
        idx += 1

        if switch == 'up':
            t += 1  # up이면 증가하다가 down이면 감소
        else:
            t -= 1

        if t == n - 1:
            switch = 'down'

        if t == 0:
            switch = 'up'

    if switch == 'up':
        t = 0
    else:
        t = n - 1

print(li)


