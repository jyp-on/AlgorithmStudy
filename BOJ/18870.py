N = int(input())

x = list(map(int, input().split()))
x2 = sorted(list(set(x)))
등수 = dict() #등수 딕셔너리


for i in range(len(x2)):
    등수[x2[i]] = i
for i in x:
    print(등수[i], end=' ')




