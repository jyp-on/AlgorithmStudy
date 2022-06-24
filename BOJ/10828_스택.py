import sys
input = sys.stdin.readline

stack = []
command_length = int(input())

for _ in range(command_length):
    ord = input()
    ord = ord[:-1] #readline으로 받으면 끝에 개행문자가 포함되어서 제거해줘야함.

    if ord.startswith('push'):
        _, num = ord.split()
        stack.append(num)
    elif 'pop' == ord:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' == ord:
        print(len(stack))
    elif 'empty' == ord:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif 'top' == ord:
        if stack:
            print(stack[-1])
        else:
            print(-1)
