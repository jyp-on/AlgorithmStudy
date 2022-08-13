test_n = int(input())

for _ in range(test_n):
    n, m = map(int, input().split())

    q = list(map(int, input().split()))

    q_ = [0 for i in range(n)]
    q_[m] = 1 #찾을 값 위치

    cnt = 0
    while True:
        if q[0] == max(q): #q의 0번쨰가 최대값이면
            cnt += 1
            if q_[0] == 1: #찾는 중요도일떄떄
               print(cnt)
               break
            else:
                del q[0]
                del q_[0]
        else:
            q.append(q[0])
            del q[0]
            q_.append(q_[0])
            del q_[0]



