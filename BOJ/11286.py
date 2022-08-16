import sys
import heapq as hq #기본적으로 min힙 지원
input = sys.stdin.readline
heap = []
N = int(input()) #연산의 개수.


for _ in range(N):
    num = int(input())
    if num != 0:
        hq.heappush(heap, (abs(num), num)) #절대값과 원래 숫자를 튜플로 넣어줌.
    else:
        try:
            print(hq.heappop(heap)[1]) #hq는 튜플의 첫번째로만 비교, 절대값 제일 작은걸 없애며 실제값을 출력
        except:
            print(0)