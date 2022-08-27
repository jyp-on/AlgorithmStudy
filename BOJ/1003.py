zero = [1, 0, 1] # fibo(0, 1, 2)의 0과 1의 개수를 미리 만들어 놓음. DP
one = [0, 1, 1]


def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num], one[num])


T = int(input())

for _ in range(T):
    fibo(int(input()))