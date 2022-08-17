n, m = list(map(int, input().split()))
s = []
중복 = []
def dfs():
    if len(s) == m:
        문자열 = ' '.join(map(str, sorted(s)))
        if 문자열 in 중복:
            return
        else:
            print(문자열)
            중복.append(문자열)
            return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()