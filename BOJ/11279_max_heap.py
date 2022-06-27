import sys
import heapq as hq
input = sys.stdin.readline
heap = []
N = int(input()) #연산의 개수.

for _ in range(N):
    tmp = int(input())
    if (tmp!=0): #들어온게 자연수이고 0이 아닐때
        hq.heappush(heap,(-tmp)) #heapq는 min 힙만 지원하기때문에 음수로 바꿔서 저장해줌.
    if (tmp==0) & (len(heap)!=0): #들어온게 0이고 리스트가 비어있지 않을때
        print(-1 * hq.heappop(heap)) #음수로 저장된 값중에 제일 작은것이 양수로 바꿧을때 가장 큰값이기 떄문에 음수로 바꿔서 출력
    elif (tmp==0) & (len(heap)==0): #들어온게 0이고 리스트가 비어있을때
        print(0)


