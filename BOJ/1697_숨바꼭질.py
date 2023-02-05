from collections import deque
n,k=map(int,input().split())
dq=deque()
dist=[0]*100001
def bfs():
    dq.append(n)
    while dq:
        now=dq.popleft()
        if now==k:
            print(dist[now])
            return
        for next in (now-1,now+1,now*2):
            if 0<=next<100001 and dist[next]==0:  # 처음 가는 곳이고 맵 안에 있다면.
                dist[next]=dist[now]+1
                dq.append(next)
bfs()