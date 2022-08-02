while True:
    n, m = map(int, input().split())
    if n==0 & m==0:
        break

    if (n%m ==0) | (m%n== 0):
        if n<=m:
            print('factor')
        else:
            print('multiple')
    else:
        print('neither')
