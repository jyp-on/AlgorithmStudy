s = input().split('-')

num = []
for i in s:
    hap = 0
    a = i.split('+')
    for k in a:
        hap += int(k)
    num.append(hap)

ans = num[0]
for i in num[1:]:
    ans -= i
print(ans)