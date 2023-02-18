# import itertools
# n = int(input())
# arr = list(map(int, input().split()))
# a, b, c, d = map(int, input().split())
# op = ['+'] * a + ['-'] * b + ['*'] * c + ['//'] * d
#
# temp_list = []
# for i in itertools.permutations(op, n-1):
#     temp = arr[0]
#     idx = 1
#     for k in i:
#         if k == '+':
#             temp += arr[idx]
#             idx += 1
#         if k == '-':
#             temp -= arr[idx]
#             idx += 1
#         if k == '*':
#             temp *= arr[idx]
#             idx += 1
#         if k == '//':
#             if (temp < 0) and (arr[idx] > 0):
#                 q = abs(temp) // arr[idx]
#                 temp = ((-1) * q)
#             elif (temp > 0) and (arr[idx] < 0):
#                 q = temp // abs(arr[idx])
#                 temp = ((-1) * q)
#             else:
#                 temp //= arr[idx]
#
#             idx += 1
#
#     temp_list.append(temp)
#     if idx > len(arr) - 1:
#         continue
#
# print(max(temp_list))
# print(min(temp_list))


# 백트래킹 dfs
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //
#
# maximum = -1e9
# minimum = 1e9
#
#
# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return
#
#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
#
#
# dfs(1, num[0], op[0], op[1], op[2], op[3])
# print(maximum)
# print(minimum)

print(int(-5/4))