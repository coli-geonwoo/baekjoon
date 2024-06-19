# 벽부수고 이동하기4 => 단순 bfs 시간 초과

from collections import deque
from collections import defaultdict
import sys

#input = lambda: sys.stdin.readline().strip('\n')

dx=[-1,1,0,0]
dy = [0,0,-1,1]

n,m= map(int, input().split())

data = [list(map(int, list(input()))) for _ in range(n)]

def bfs(x,y, id):
  cnt=0
  q=deque([(x,y)])
  dp[x][y]=id

  while(q):
    a,b = q.popleft()
    cnt+=1

    for i in range(4):
      nx= a+dx[i]
      ny= b+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m or  dp[nx][ny]!=0 or data[nx][ny]!=0:
        continue
      dp[nx][ny]=id
      q.append((nx, ny))
  return cnt

dp=[[0] *m for _ in range(n)]

movable=[0]

group_id = 1

for i in range(n):
  for j in range(m):
    if data[i][j]==0 and dp[i][j]==0:
      t =bfs(i,j, group_id)
      movable.append(t)
      group_id+=1

for i in range(n):
  for j in range(m):
    if data[i][j]!=0:
      temp=1
      ids=set()
      for k in range(4):
        nx= i+dx[k]
        ny= j+dy[k]
        if nx<0 or ny<0 or nx>=n or ny>=m or data[nx][ny]!=0:
          continue
        ids.add(dp[nx][ny])
      for id in ids:
        temp+=movable[id]
      data[i][j] = temp%10

for i in range(n):
  for j in range(m):
    print(data[i][j], end='')
  print()