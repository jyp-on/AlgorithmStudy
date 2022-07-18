N = int(input())
li = list(map(int, input().split()))

def isprime(x):
    if x == 1:
        return False
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True

sum = 0
for i in range(len(li)):
    if isprime(li[i]) == True:
        sum+=1
print(sum)