N = int(input())

def check(word):
    쓴글자 = []
    직전글자 = ''
#쓴글자에 있고 직전글자이면 가능.
#쓴글자에 있는데 직전글자가 아니면 false반환
    for i in range(len(word)):

        if word[i] in 쓴글자: #word가 쓴글자에 포함되있으면
           if word[i] != 직전글자: #word가 쓴글자에 포함되있고 직전글자가 아니면
               return False

        else: # 한번도 안쓴글자
            쓴글자.append(word[i])
            직전글자 = word[i]

sum = 0
for _ in range(N):
    word = input()
    if check(word) != False:
        sum += 1
print(sum)



