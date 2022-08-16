# 찾는 숫자를 행으로 나눈 몫이 해당 열에서 찾는 숫자보다 작거나 같은 수의 개수이다.
n = int(input())
k = int(input())

def binary_search(target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n) # 각 행에서 임의의 수보다 작은 수의 개수

        if cnt >= target:
            end = mid-1
        else:
            start = mid+1
    return start


print(binary_search(k,1,n*n)) # N제곱보다 작은 수이므로 최대값은 N제곱으로.