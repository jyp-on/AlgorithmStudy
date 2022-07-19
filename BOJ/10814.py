N = int(input())

회원들 = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    회원들.append([age, name, i])

가입순 = sorted(회원들, key=lambda x:x[2])
나이순 = sorted(가입순, key=lambda x:x[0])


for i in 나이순:
    print(i[0], i[1])


