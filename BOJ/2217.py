N = int(input())

rope = []

for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

w = []
for i in range(N):
    w.append(rope[i] * (i+1))
print(max(w))