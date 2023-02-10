import itertools
T = [0] * 50
T[1] = 1
n = 2
for i in range(2, 50):
    T[i] = T[i-1] + n
    n += 1
T = T[1:]

case = int(input())

for _ in range(case):
    target = int(input())
    Find = False
    for i in itertools.combinations_with_replacement(T, 3): # 순서만 바뀐것은 같은걸로봄.
        if sum(i) == target:
            print(1)
            Find = True
            break
    if not Find:
        print(0)
