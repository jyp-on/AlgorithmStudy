
n = int(input()) #피보나치 수
pivo = [0, 1]
for i in range(n):
    pivo.append(pivo[i] + pivo[i+1])
print(pivo[n])

