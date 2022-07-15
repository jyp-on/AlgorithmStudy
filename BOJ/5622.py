s = input()
time = []
for i in range(len(s)):
    if s[i] in 'ABC':
        time.append(3)
    elif s[i] in 'DEF':
        time.append(4)
    elif s[i] in 'GHI':
        time.append(5)
    elif s[i] in 'JKL':
        time.append(6)
    elif s[i] in 'MNO':
        time.append(7)
    elif s[i] in 'PQRS':
        time.append(8)
    elif s[i] in 'TUV':
        time.append(9)
    elif s[i] in 'WXYZ':
        time.append(10)
print(sum(time))

