n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
s = 0
for i in range(len(b)):
    s += a[i] * max(b)
    b.pop(b.index(max(b)))
print(s)