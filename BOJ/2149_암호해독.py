import sys
key = sys.stdin.readline().rstrip('\n') # 키를 입력 받습니다.
encoded_text = sys.stdin.readline().rstrip('\n') # 암호화 된 문장을 입력 받습니다.
lines = len(encoded_text) // len(key) #
sort_key = sorted(key) # 알파벳 순으로 키를 정렬합니다.
print(f'sort_key {sort_key}')
decoded_dict = dict() # 사람 보기 좋으라고 딕셔너리 생성
for i in range(len(key)):
	# 사람 보기 좋으라고 몇 번째 인덱스에 어떤 문자 + 그 문자와 같은 인덱스 였던 문자들을 합쳐줍니다.
    	# 다시 한다면 그냥 list 에 넣고 enumerate 로 찍어 보고 말았을 것 같군요..
    decoded_dict[i] = sort_key[i] + encoded_text[lines*i:lines*(i+1)]
print(f'decoded_dict {decoded_dict}')
# 딕셔너리에 넣은 값 중 value 값만 따로 빼서 리스트로 저장합니다.
values = list(decoded_dict.values())
# 얘도 위에서 선언한 딕셔너리와 같은 이유 입니다..
plain_dict = dict()

for i in range(len(key)):
    for j in range(len(values)):
        if key[i] == values[j][0]: #딕셔너리로 저장해놓은 값의 앞 글자와 키의 앞 글자가 같다면,
            plain_dict[i] = values.pop(j) #키에 같은 알파벳이 있을 수 있으니 리스트에서 값을 제거하여 plain_dict 에 넣고
            break # 다음 키에 대해 맞는 값을 찾도록 가장 안쪽 반복문을 탈출합니다.

for i in range(1, lines+1): # 첫 번째 값에 사람 보기 좋으라고 키의 알파벳을 넣어 놨으니 1부터 시작해서
    for j in list(plain_dict.values()):
        print(j[i], end='') # 이전 반복문에서 원래 순서대로 정리한 값을 출력합니다.