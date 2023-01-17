# 현재 나이트의 위치
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 이동가능한 dx, dy 정의
steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

cnt = 0

for step in steps:
    temp_row = row + step[0]
    temp_col = column + step[1]
    if (temp_row > 0 & temp_row < 9) & (temp_col > 0 & temp_col < 9):
        cnt += 1

print(cnt)
