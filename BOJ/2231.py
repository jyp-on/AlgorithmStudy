N = input()

생성자들 = []


검사시작 = int(N) - len(N)*9

for i in range(1, int(N), 1):
    합 = int(i)
    for k in range(len(str(i))):
        합 += int(str(i)[k])


    if 합 == int(N):
        생성자들.append(int(i))

if 생성자들:
    print(생성자들[0])
else:
    print(0)

