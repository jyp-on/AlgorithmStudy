import sys
import heapq as hq #기본적으로 min힙 지원
input = sys.stdin.readline
heap = []
N = int(input()) #연산의 개수.

for _ in range(N):
    tmp = int(input())
    if (tmp!=0): #들어온게 자연수이고 0이 아닐때
        hq.heappush(heap,(tmp)) #heapq는 min 힙만 지원하기때문에 음수로 바꿔서 저장해줌.
    if (tmp==0) & (len(heap)!=0): #들어온게 0이고 리스트가 비어있지 않을때
        print(hq.heappop(heap)) #가장 작은값 pop시키며 출력
    elif (tmp==0) & (len(heap)==0): #들어온게 0이고 리스트가 비어있을때
        print(0)