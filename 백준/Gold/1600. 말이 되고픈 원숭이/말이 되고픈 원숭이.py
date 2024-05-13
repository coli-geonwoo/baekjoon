import sys
from collections import deque

dx=[-1,1,0,0, 2, 2 , -2, -2, 1,1, -1, -1]
dy=[0,0,-1,1, 1 , -1, 1, -1,2,-2 ,2, -2]

k= int(input())
m,n= map(int, input().split())

data= [list(map(int, input().split())) for _ in range(n)]

visited = [[[sys.maxsize]*(k+1) for _ in range(m)]  for _ in range(n)]

def bfs():
  q= deque([(0,0,0,0)])
  visited[0][0][0] = 0

  while(q):
    chance, distance, x, y, =q.popleft()

    for i in range(12):
      nx = x+dx[i]
      ny= y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m or data[nx][ny] ==1:
        continue

      if i<4 and visited[nx][ny][chance] > distance+1:
        visited[nx][ny][chance] = distance+1
        q.append((chance, distance+1, nx, ny))
        continue

      if i>=4 and chance<k and visited[nx][ny][chance+1] > distance+1:
        visited[nx][ny][chance+1] = distance+1
        q.append((chance+1, distance+1, nx, ny))
  
  return min(visited[n-1][m-1])


result= bfs()

if result ==sys.maxsize:
  print(-1)
else:
  print(result)
