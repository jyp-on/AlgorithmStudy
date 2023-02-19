a, b, c = 0, 0, 0
e, s, m = map(int, input().split())
ans = 0

while True:

    a = (a + 1)
    if a == 16:
        a = 1
    b = (b + 1)
    if b == 29:
        b = 1
    c = (c + 1)
    if c == 20:
        c = 1
    ans += 1

    if a == e and b == s and c == m:
        break


print(ans)

