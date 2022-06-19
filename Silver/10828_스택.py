stack = []
command_length = int(input())
while command_length!=0:
    ord = input()

    if 'push' == ord[0:4]:
        stack.push(ord[5])
    if 'top' == ord:






def size():
    return len(stack)
def empty():
    if size() == 0:
        return 1
    else:
        return 0
def top():
    return stack[0]

