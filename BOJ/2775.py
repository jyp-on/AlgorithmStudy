import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    층 = int(input())
    호 = int(input())
    people = [i for i in range(1, 호+1)] #0층에 사는 사람들
    for x in range(층):
        for y in range(1, 호):
            people[y] += people[y-1]
            print(people)
            # print(people[-1])




