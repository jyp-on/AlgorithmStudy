

while True:
    a, b, c = map(int, input().split())
    li = [a, b, c]
    li = sorted(li)

    if li[0] == 0 & li[1] == 0 & li[2] ==0:
        break

    if (li[0]*li[0]) + (li[1]*li[1]) == li[2]*li[2]:
        print('right')
    else:
        print('wrong')


