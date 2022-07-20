S = input()

문자열조합 = []
for i in range(len(S)):
    for k in range(i, len(S)+1):
        문자열조합.append(S[i:k])
print(len(set(문자열조합))-1)