import sys
from collections import deque

n,m= map(int, input().split())

data = [list(input()) for _ in range(n)]

dx=[-1,0,1, 0,-1, 1, -1, 1]
dy=[ 1,1,1,-1, 0,-1,-1, 0]


def bfs(x,y):
  visited= [[sys.maxsize]*m for _ in range(n)]
  visited[x][y]=0
  q=deque([(0,x,y)])

  while(q):
    distance, x, y = q.popleft()

    for i in range(8):
      nx= x+dx[i]
      ny=y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m or data[nx][ny]=="#":
        continue
      
      if i<=2 and visited[nx][ny] > distance:
        visited[nx][ny]=distance
        q.append((distance, nx, ny))
        #print(nx, ny, distance)
      elif i>=3 and visited[nx][ny] > distance+1:
        visited[nx][ny]= distance+1
        q.append((distance+1, nx, ny))
        #print(nx, ny, distance)
  
  if visited[endx][endy]==sys.maxsize:
    return -1
  else:
    return visited[endx][endy]

startx=0
starty=0
endx=0
endy=0
for i in range(n):
  if "K" in data[i]:
    startx=i
    starty=data[i].index("K")
  if "*" in data[i]:
    endx=i
    endy= data[i].index("*")

print(bfs(startx, starty))
    