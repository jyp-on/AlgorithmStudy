def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n = int(input())
item = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

item.sort()
orders.sort()

for order in orders:
    if binary_search(item, order, 0, n-1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
