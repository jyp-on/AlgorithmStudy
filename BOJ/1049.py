n, m = map(int, input().split())

packages = []
ones = []
for i in range(m):
    package, one = map(int, input().split())
    packages.append(package)
    ones.append(one)

res = 0

if min(ones) * 6 >= min(packages): #6으로 나눈 나머지 가격이 개별이 더 비싸면
    res = (n // 6) * min(packages) + (n % 6) * min(ones) #패키지로 사다가 남은것들 낱개로
    if (n % 6) * min(ones) > min(packages): #만약에 패키지로 했다가 나머지들 사는것보다 패키지 한개 더 사는게 싸다면 패키지 구입
        res = ((n // 6) + 1) * min(packages)
elif min(ones) * 6 < min(packages): #개별이 더 싸면 모두 낱개로 산다.
    res = (n * min(ones))

print(res)