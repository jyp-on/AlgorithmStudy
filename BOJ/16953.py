a, b = input().split()
cnt = 0

while True:
    if b == a:
        break
    if int(a) > int(b):
        print(-1)
        exit()

    if int(b) % 2 == 0:
        b = str(int(b) // 2)
        cnt += 1
    elif b[-1] == '1':
        b = b[0:-1]
        cnt += 1
    else:
        print(-1)
        exit()

print(cnt+1)