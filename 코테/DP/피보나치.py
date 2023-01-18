#  1. 큰 문제를 작은 문제로 나눌 수 있다.
#  2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

#  메모이제이션 -> 한번 구한 결과를 메모리 공간에 메모해두고 필요할 때 이 결과를 그대로 가져오는 방식. 캐싱이라고도 함.

#  재귀함수를 이용한 피보나치 수열 DP

# d = [0] * 501
#
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     #  이미 한번 계산 된 문제라면 그대로 반환
#     if d[x] != 0:
#         return d[x]
#
#     #  메모이제이션
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]
#
# print(fibo(500))


#  반복문을 이용한 피보나치수열 DP bottom up 방식
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])


