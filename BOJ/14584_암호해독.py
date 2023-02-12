import sys
input = sys.stdin.readline
def calc(key, n, words):
    for i in range(26):
        temp = ""
        for k in key:
            #1~26까지 카이사르 복호화한 것을 탐색해봄
            temp += chr(((ord(k)-ord('a')+i) % 26) + 97)
        for k in range(n):
            if words[k] in temp: # 해당 문자열이 temp에 포함되어있는지 확인
                return temp

def main():
    key = input().rstrip()
    n = int(input())
    words = []
    for i in range(n):
        word = input().rstrip()
        words.append(word)

    print(calc(key, n, words))

main()