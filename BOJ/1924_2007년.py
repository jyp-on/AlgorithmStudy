day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day_idx = 0

x, y = map(int, input().split())
s_x, s_y = 1, 1

while s_x != x or s_y != y:
    if s_x in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif s_x in [2]:
        max_day = 28
    else:
        max_day = 30

    s_y += 1
    day_idx += 1

    if s_y > max_day:
        s_y = 1
        s_x += 1


print(day[day_idx % 7])



