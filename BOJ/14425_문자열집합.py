import sys
input = sys.stdin.readline
N, M = map(int, input().split())

S = []
for i in range(N):
    S.append(input())

m_list = []
for k in range(M):
    m_list.append(input())

# m_list = list(m_list) #중복제거

cnt = 0
for i in m_list:
    if i in S:
        cnt += 1

print(cnt)