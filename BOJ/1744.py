n = int(input())

num = [int(input()) for i in range(n)]

q1 = [] #0보다 작은것들
q2 = [] #0보다 큰것들
q3 = [] #0

for i in num:
    if i < 0:
        q1.append(i)
    elif i == 0:
        q3.append(i)
    else:
        q2.append(i)

q1.sort()
q2.sort()

res = 0

while True:
    if len(q2) < 2:
        break
    if q2[-1] * q2[-2] > q2[-1] + q2[-2]: #가장 큰수와 그 다음 큰수를 곱한게 더한거보다 클떄
        res += q2[-1] * q2[-2]
        q2.pop()
        q2.pop()
    else:
        res += q2[-1] + q2[-2]
        q2.pop()
        q2.pop()

res += sum(q2)


while True:
    if len(q1) == 0:
        break

    if len(q1) >= 2: ##음수가 2의 배수개만큼 있으면 큰거끼리 곱해서 더하고
        res += q1[0] * q1[1]
        q1.pop(0)
        q1.pop(0)
    elif (len(q1) == 1): #음수가 1개일 경우, 0이 있다면 곱하고 아니면 그냥 더함
        if (len(q3) != 0):
            res += q1.pop() * q3.pop()
        else:
            res += sum(q1)

print(res)