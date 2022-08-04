import sys
input = sys.stdin.readline

for _ in range(int(input())):
    queue = []
    괄호문자열 = input().strip()

    미리끝났는지 = False

    for i in 괄호문자열:
        if i == ')':
            if len(queue) == 0:
                print('NO')
                미리끝났는지 = True
                break
            else:
                queue.pop()

        else:
            queue.insert(0, i)

    if 미리끝났는지:
        pass
    else:
        if len(queue) == 0:
            print('YES')
        else:
            print('NO')


