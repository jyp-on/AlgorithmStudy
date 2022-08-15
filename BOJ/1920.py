N = int(input())
A = sorted(list(map(int, input().split())))

M = int(input())
B = list(map(int, input().split()))

def 이진탐색(l, A, start, end): #l = 찾는값 A = 찾는 범위
    if start > end:
        return 0 #못찾는 경우이므로 0 return
    m = (start+end) // 2

    if l == A[m]:
        return 1 #정확히 일치하는경우 이므로 1 return
    elif l < A[m]:
        return 이진탐색(l, A, start, m-1)
    else:
        return 이진탐색(l, A, m+1, end)

for l in B:
    start = 0
    end = len(A)-1
    print(이진탐색(l, A, start, end))



