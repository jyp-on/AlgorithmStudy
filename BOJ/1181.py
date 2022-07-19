N = int(input())

word_list = []
for _ in range(N):
    word_list.append(input())

word_list = list(set(word_list)) #중복제거

사전정렬 = sorted(word_list)
길이정렬 = sorted(사전정렬, key=len)

for i in 길이정렬:
    print(i)

