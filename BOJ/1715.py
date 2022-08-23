import heapq
n = int(input())

cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
s = []
while len(s) != n-1:
    r = heapq.heappop(cards) + heapq.heappop(cards)
    s.append(r)
    heapq.heappush(cards, r)
print(sum(s))
