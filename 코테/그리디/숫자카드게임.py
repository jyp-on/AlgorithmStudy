import time
n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
start_time = time.time()
#프로그램 소스코드 시작
min_list = []

for i in range(n):
    min_list.append(min(li[i]))

print(max(min_list))
# 프로그램 소스코드 끝
end_time = time.time()
print("time :", end_time - start_time)


