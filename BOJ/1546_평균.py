N = int(input())

score = list(map(int, input().split()))

M = max(score)

조작된점수들 = []
for i in score:
    i = i/M*100
    조작된점수들.append(i)


print(sum(조작된점수들)/len(조작된점수들))