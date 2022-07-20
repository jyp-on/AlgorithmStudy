from collections import defaultdict

N = int(input())

n_list = list(map(int, input().split()))

dic = defaultdict(int)

for i in n_list:
    dic[i] += 1

M = int(input())

m_list = list(map(int, input().split()))

for i in m_list:
    print(dic[i], end=' ')