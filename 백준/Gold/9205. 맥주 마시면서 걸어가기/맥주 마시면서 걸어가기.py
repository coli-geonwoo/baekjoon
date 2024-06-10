import sys
input = lambda: sys.stdin.readline().strip('\n')

#맥주 마시면서 걸어가기
from collections import deque

def bfs():
  q= deque([[hx, hy]])  

  while(q):
    x,y= q.popleft()

    if abs(x-fx)+abs(y-fy)<=1000:
      print("happy")
      return
    
    for i in range(n):
      if visited[i]==0:
        sx, sy= store[i]
        if abs(sx-x)+abs(sy-y)<=1000:
          q.append([sx, sy])
          visited[i]=1
  print("sad")
  return
t= int(input())

for _ in range(t):
    n= int(input())
    visited=[0]*n
    hx, hy= map(int, input().split())
    store= [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    bfs()