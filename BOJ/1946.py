import sys
input = sys.stdin.readline
T = int(input())

for i in range(T) :
    n = int(input())
    people_lst = [0]*n
    for j in range(n) :
            t1 ,t2 = map(int,input().split())
            people_lst[j] = [t1,t2]

    people_lst_sorted_0 = sorted(people_lst, key = lambda x : x[0])
    hired = 1
    man = people_lst_sorted_0[0][1] #서류심사 1등의 면접점수를 저장.
    for j in range(1,n) :
        if people_lst_sorted_0[j][1] < man : #면접등수가 더 높으면
            man = people_lst_sorted_0[j][1] #man(뽑힌사람) 의 등수를 변경
            hired += 1

    print(hired)