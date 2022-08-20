a = int(input())
n = 1
while n * (n + 1) / 2 <= a: #1부터 n까지의 합공식
    n += 1
print(n - 1)