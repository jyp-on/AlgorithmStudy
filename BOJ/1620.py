import sys
input = sys.stdin.readline

N, M = map(int, input().split())

도감 = dict()

for i in range(N):
    a = input().rstrip() #공백제거
    도감[a] = i+1
    도감[i+1] = a


for k in range(M):
    질문 = input().rstrip()
    if 질문.isdigit():
        print(도감[int(질문)])
    else:
        print(도감[질문])
