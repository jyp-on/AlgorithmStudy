def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):	# 2부터 x-1까지의 모든 숫자
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []

for i in all_list:
    if isprime(i):
        memo.append(i)

N = int(input())
while True:
    sum = 0
    if N==0:
        break
    for i in memo:
        if N<i<=2*N:
            sum+=1
    print(sum)
    N=int(input())