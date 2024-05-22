#4179. 불!

from collections import deque
import sys
import copy

n,m= map(int, input().split())

data= [list(input()) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(jihoonx, jihoony, fires):

  fireq=deque()

  for fx, fy in fires:
    fireq.append((fx, fy))

  next_fireq=deque()
  jihoonq = deque([(0, jihoonx, jihoony)])
  next_jihoon_q = deque()
  result=sys.maxsize

  while not (len(jihoonq) ==0 and len(next_jihoon_q)==0):
    #불 옮기기
    while(fireq):
      x, y = fireq.popleft()
      for i in range(4):
        nx = x+dx[i]
        ny= y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
          continue
        
        if data[nx][ny] =="." or data[nx][ny]=="J":
          data[nx][ny] ="F"
          next_fireq.append((nx, ny))
    
    while(jihoonq):
      dist,x,y = jihoonq.popleft()
      #도착 시
      if x==0 or y==0 or x==n-1 or y==m-1:
        result= min(dist, result)
      
      for i in range(4):
        nx= x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
          continue
        
        if data[nx][ny]==".":
          data[nx][ny]="J"
          next_jihoon_q.append((dist+1, nx, ny))
  


    fireq= next_fireq
    next_fireq= deque()

    jihoonq= next_jihoon_q
    next_jihoon_q=deque()
  
  return result


jihoonx=jihoony=0
fires=[]
for i in range(n):
  for j in range(m):
    if data[i][j]=="J":
      jihoonx=i
      jihoony=j
    if data[i][j]=="F":
      fires.append((i, j))

result= bfs(jihoonx, jihoony, fires)

if result==sys.maxsize:
  print("IMPOSSIBLE")
else:
  print(result+1)
