N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
    h = (start + end) // 2 #시작점
    tree_len = 0 #나무 m

    for i in tree: #톱보다 위에있는거만 자름.
        if i >= h:
            tree_len += (i - h)

    if tree_len >= M: #나무길이가 구하는 거보다 적을때
        start = h + 1
    else:
        end = h - 1
print(end)

