import sys
input = sys.stdin.readline


length = int(input())
n_list = [0] * 10001

for _ in range(length):
    n_list[int(input())] += 1 #입력값과 같은 인덱스에 +1을 해줌.

for i in range(10001):
    if n_list[i] > 0:
        for j in range(n_list[i]): #1번자리에 2개가 들어가면 1을 2개출력
            print(i)


