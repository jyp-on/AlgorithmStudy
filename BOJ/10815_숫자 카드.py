import sys
input = sys.stdin.readline

N = int(input())
n1_list = list(map(int, input().split()))
M = int(input())
n2_list = list(map(int, input().split()))

n1_list.sort() #카드 정렬

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(M):
    if binary_search(n1_list, n2_list[i], 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
