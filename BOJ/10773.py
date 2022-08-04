import sys
input = sys.stdin.readline

queue = []

for i in range(int(input())):
    a = int(input())
    if a != 0:
        queue.insert(0, a)
    else:
        queue.pop(0)
print(sum(queue))