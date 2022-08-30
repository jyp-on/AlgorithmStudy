s = input()
s = s + '00000000000000000000'
search = input()
start = 0
end = len(search)
cnt = 0
for i in range(len(s)):
    if search == s[start:end]:
        cnt += 1
        start = end
        end = end + len(search)
    else:
        start+=1
        end+=1

print(cnt)