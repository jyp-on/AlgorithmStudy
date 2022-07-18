import math
min_ = int(input())
max_ = int(input())

def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x-1까지의 모든 숫자
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True

sum_list = []
for i in range(min_, max_+1, 1):
    if isprime(i) == True:
        sum_list.append(i)

if sum_list:
    print(sum(sum_list))
    print(sum_list[0])
else:
    print(-1)