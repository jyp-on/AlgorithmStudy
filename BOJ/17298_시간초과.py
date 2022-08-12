N = int(input())
A = list(map(int, input().split()))

for idx, item in enumerate(A):
    temp = []
    if idx < len(A)-1:
        for id, it in enumerate(A[idx+1:]):

            if item < it:
                temp.append((it, id))
            elif item == max(A):
                print(-1, end =' ')
                break

    elif idx == len(A)-1:
        print(-1)

    temp.sort(key=lambda x:x[1])
    if temp:
        print(temp[0][0], end=' ')