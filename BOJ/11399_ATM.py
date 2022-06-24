import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()

for i in range(n):
    for k in range(i + 1):
        num += s[k]
print(num)




