N = int(input())
cnt = 0
def is한수(n):
    if n <= 99:
        return True
    n = str(n)
    if len(n) == 3:
        if (int(n[0]) - int(n[1])) == (int(n[1]) - int(n[2])):
            return True
        else:
            return False
    else:
        return False

for i in range(1, N+1):
    if is한수(i):
        cnt+=1
print(cnt)

