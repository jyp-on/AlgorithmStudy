import sys
input = sys.stdin.readline

N = int(input())
정답 = 2
비교대상 = 7
간격 = 12
if N==1:
    print(1)
    exit()
while True:

    if N <= 비교대상:
        print(정답)
        break
    else:
        비교대상+=간격
        간격+=6
        정답+=1