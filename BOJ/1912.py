N = int(input())

num = list(map(int, input().split()))

s = [num[0]]

for i in range(0, N-1):
    s.append(max(s[i]+num[i+1], num[i+1]))
print(max(s))