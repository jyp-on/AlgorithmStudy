import sys, math
input = sys.stdin.readline

N = []
for _ in range(int(input())):
    N.append(int(input()))

def find(i):
    temp = set()
    for k in N:
        temp.add(k%i)
        if len(temp)>1:
            return
    if len(temp)==1:
        print(i, end= ' ')


