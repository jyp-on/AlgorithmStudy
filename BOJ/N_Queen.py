import sys
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 같은열이거나 대각선 위치 상에 있으면 False.
            return False

    return True
def n_queens(x):
    global ans
    if x == n:
        ans += 1
        # print(row)

    else:
        for i in range(n): # i는 열번호 0부터 n-1까지 옮겨가며 유망한곳 찾기.
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n = int(sys.stdin.readline().rstrip())
ans = 0
row = [0] * n

n_queens(0)
print(ans)