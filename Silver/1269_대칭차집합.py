import sys
input = sys.stdin.readline

a, b = map(int, (input().split()))

li1 = list(map(int, input().split()))

li2 = list(map(int, input().split()))

sym_diff = list(set(li1) ^ set(li2))
print(len(sym_diff))