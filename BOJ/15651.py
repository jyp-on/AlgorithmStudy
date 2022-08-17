n, m = list(map(int, input().split()))
s = []
중복 = []
def dfs():
    if len(s) == m:
        문자열 = ' '.join(map(str, s))
        print(문자열)
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

dfs()