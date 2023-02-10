import itertools
arr = []
for _ in range(9):
    arr.append(int(input()))
for i in itertools.combinations(arr, 7): # 7명 중복없이 뽑아준다.
    if sum(i) == 100:
        for k in sorted(i):
            print(k)
        break # 반복문 탈출


