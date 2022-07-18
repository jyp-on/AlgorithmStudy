alpha = 'abcdefghijklmnopqrstuvwxyz'
N = list(input())

for i in alpha:
    if i in N:
        print(N.index(i), end=' ')
    else:
        print(-1, end=' ')