t = int(input())

for i in range(t):
    c = int(input())


    print(c // 25, end=' ')
    c = c % 25
    print(c // 10, end=' ')
    c = c % 10
    print(c // 5, end=' ')
    c = c % 5
    print(c // 1, end=' ')

    print()

