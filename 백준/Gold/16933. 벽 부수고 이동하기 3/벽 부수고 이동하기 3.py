#1은 이동할 수 없는 벽이 있는 것

# 낮, 밤이고, 낮에만 이동가능 => 변수가 하나씩 추가
# k개까지 부수고 이동가능

from collections import deque
import sys

INF= sys.maxsize
n,m,k= map(int, input().split())

data=[list(map(int, list(input()))) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
  dp= [[[INF]*m for _ in range(n)] for _ in range(k+1)]
  q=deque()
  q.append((0,0, 0,0,0))

  for i in range(k+1):
    dp[i][0][0]=0
  

  while(q):
    canMove, chance, dist, x, y = q.popleft()

    for i in range(4):
      nx= x+dx[i]
      ny= y+dy[i]
      
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      
      if data[nx][ny]==0:
        if canMove==0 and chance<=k and dp[chance][nx][ny] > dist+1:
            dp[chance][nx][ny]=dist+1
            q.append((1, chance, dist+1, nx, ny))
        elif canMove==1 and chance<=k and dp[chance][nx][ny] > dist+1:
            dp[chance][nx][ny]=dist+1
            q.append((0, chance, dist+1, nx, ny))
        
      else:
        if canMove==0 and chance<k and dp[chance+1][nx][ny] > dist+1:
            dp[chance+1][nx][ny]= dist+1
            q.append((1, chance+1, dist+1, nx, ny))
        elif canMove==1 and chance<k:
            q.append((0, chance, dist+1, x,y)) #머무르기
  
  result = INF
  for i in range(k+1):
    result= min(result, dp[i][n-1][m-1])

  if result==INF:
    return -1
  return result+1


print(bfs())
          




