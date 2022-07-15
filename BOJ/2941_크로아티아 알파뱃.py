s = input()
s += '000'
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
len_cnt = 0
while True: #0 ~ 8
    if len_cnt == len(s)-2:
        break

    if s[len_cnt] == '0':
        break

    if s[len_cnt]+s[len_cnt+1] in cro:
        cnt+=1
        len_cnt+=2
        continue
    elif s[len_cnt]+s[len_cnt+1]+s[len_cnt+2] in cro:
        cnt+=1
        len_cnt+=3
        continue
    else:
        cnt+=1
        len_cnt+=1
        continue


print(cnt)