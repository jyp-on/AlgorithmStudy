from collections import deque


d1 = deque()
d2 = deque()

arr = []

item1 = list(input().split())
item2 = list(input().split())

for i in item1:
    d1.append(i)
for i in item2:
    d2.append(i)
d1.extend(d2)
print(*sorted(d1))



