#14442. 벽 부수고 이동하기2

from collections import deque
import sys
input = lambda: sys.stdin.readline().strip('\n')

n,m,k = map(int, input().split())

visited= [[[sys.maxsize]*(k+1) for _ in range(m)] for _ in range(n)]

data= [list(map(int, list(input()))) for _ in range(n)] 


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,z):
  visited[x][y][z] = 1
  q=deque([(1, x,y,z)])
    

  while(q):
    distance, x,y,z = q.popleft()
    
    if x==n-1 and y==m-1:
        return distance

    for i in range(4):
      nx= x+dx[i]
      ny= y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      
      if data[nx][ny]==0 and visited[nx][ny][z]>distance+1:
        visited[nx][ny][z]=distance+1
        q.append((distance+1, nx, ny, z))
      elif data[nx][ny]==1 and z<=k-1 and visited[nx][ny][z+1]> distance+1:
        visited[nx][ny][z+1]=distance+1
        q.append((distance+1, nx, ny, z+1))
    
'''
for i in range(n):
  for j in range(m):
    print(visited[i][j][0])
'''

bfs(0,0,0)

result= min(visited[n-1][m-1])

if result == sys.maxsize:
  print(-1)
else:
  print(result)