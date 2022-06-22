length = int(input())
un_sorted = []

for _ in range(length):
    un_sorted.append(int(input()))

for j in range(length):
    for i in range(j+1, length):
        if un_sorted[j] > un_sorted[i]:
            temp = un_sorted[j]
            un_sorted[j] = un_sorted[i]
            un_sorted[i] = temp

for k in un_sorted:
    print(k)
