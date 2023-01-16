# s = input()
# alp = ['U', 'C', 'P', 'C']
# i = 0
# for a in alp:
#     if a in s:
#         i += 1
#         s = s[s.index(a) + 1:]
#     else:
#         print('I hate UCPC')
#         break
# if i == 4:
#     print('I love UCPC')
# row, col 인덱스로 탐색할 수 있게 방향 설정
#    우->하->좌->상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


N = int(input()) #크기
arr = [[0]*N for _ in range(N)]
# 초기 위치 & 회전방향 설정
r, c = 0, 0
dist = 0  # 0:우, 1:하, 2:좌, 3:상


for n in range(1, N*N + 1):
    arr[r][c] = n
    r += dr[dist]
    c += dc[dist]

    # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
    # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
    # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
    if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != 0:
        # 실행취소
        r -= dr[dist]
        c -= dc[dist]
        # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
        dist = (dist + 1) % 4
        #  다시 시작
        r += dr[dist]
        c += dc[dist]



for row in arr:
    print(*row)