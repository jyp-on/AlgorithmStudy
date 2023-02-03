def solution(maps):
    answer = []

    col = len(maps[0])
    row = len(maps)

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    graph = [[False for _ in range(col)] for _ in range(row)]  # 방문 여부 체크

    y, x = 0, 0  # row, col

    temp = 0

    if len(set(maps)) == 1:  # 전부 X인경우
        return [-1]

    # X 인경우 bfs로 숫자 나올때까지 순회.
    # 숫자가 나온경우 상 하 좌 우 숫자인곳만 순회하여 더함.
    switch = True
    while switch:

        if maps[y][x] == 'X' and not graph[y][x]:  # X 인 경우 가로로 한칸씩 증가
            graph[y][x] = True  # 방문처리
            nx = x + 1
            if nx == col - 1:  # 가로범위 넘었을 경우.
                x = 0
                y += 1
                continue
            else:
                x = nx
                continue

        if maps[y][x] != 'X' and not graph[y][x]:  # 무인도이고 방문하지 않았을 경우.
            graph[y][x] = True
            temp += int(maps[y][x])

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < col and 0 <= ny < row and not graph[ny][nx] and maps[ny][nx] != 'X':
                    # 맵을 벗어나지않고 방문하지 않고 X가 아닌경우.
                    x = nx
                    y = ny
                    break
                else:  # 갈곳이 없을경우 answer에 값 추가후 맵에서 방문하지 않은 곳으로 이동.
                    answer.append(temp)
                    temp = 0
                    miniSwitch = True
                    for r in range(row):
                        if miniSwitch:
                            for c in range(col):
                                if graph[r][c] == False:
                                    x = c
                                    y = r
                                    miniSwitch = False
                        else:
                            break

                    switch = False
        answer.sort()
        return answer


solution(["X591X","X1X5X","X231X", "1XXX1"])