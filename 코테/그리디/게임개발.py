n, m = map(int, input().split())

# 방문한 위치 저장하기위한 맵생성, 0으로 초기화
d = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X, Y, 방향 입력
x, y, direction = map(int, input().split())

d[x][y] = 1 # 현재좌표 방문처리

#전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 최전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전 하고나서 정면에 가보지 않은 칸이 존재하고 육지일경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
    else: # 회전만 증가. 이동 X
       turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        if array[nx][ny] == 0: # 뒤로 갈수있으면
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
