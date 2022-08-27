n1, n2 = input().split()
max1, max2 = '', ''
min1, min2 = '', ''

for i in range(len(n1)):
    if n1[i] == '5' or n1[i] == '6':
        max1 += '6'
        min1 += '5'
    else:
        max1 += n1[i]
        min1 += n1[i]

for i in range(len(n2)):
    if n2[i] == '5' or n2[i] == '6':
        max2 += '6'
        min2 += '5'
    else:
        max2 += n2[i]
        min2 += n2[i]


print(int(min1) + int(min2), int(max1) + int(max2))